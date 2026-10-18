#!/usr/bin/env python3
import json
import sys
from client import AgenticFreightCarbonOffsetRouter

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        router = AgenticFreightCarbonOffsetRouter()
        cargo = {"weight_kg": 100.0, "max_acceptable_days": 4}
        carriers = [
            {"carrier": "Air Cargo Express", "mode": "air_freight", "transit_days": 1, "cost_usd": 150.0, "distance_km": 1200.0},
            {"carrier": "EcoRail Freight", "mode": "rail_freight", "transit_days": 3, "cost_usd": 65.0, "distance_km": 1200.0}
        ]
        res = router.optimize_freight_and_offset(cargo, carriers)
        assert res["chosen_sustainable_route"]["carrier"] == "EcoRail Freight"
        assert res["chosen_sustainable_route"]["co2_emissions_kg"] < 10.0
        print(f"[TEST PASS] Freight Carbon Router Selected: {res['chosen_sustainable_route']['carrier']}")
        sys.exit(0)

    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            method = req.get("method")
            msg_id = req.get("id")
            if method == "initialize":
                print(json.dumps({"jsonrpc": "2.0", "id": msg_id, "result": {"serverInfo": {"name": "genpark-freight-carbon-router", "version": "1.0.0"}}}))
            elif method == "tools/list":
                print(json.dumps({"jsonrpc": "2.0", "id": msg_id, "result": {"tools": [{"name": "optimize_freight_and_offset", "description": "Sustainable freight route selection & carbon offset calculation"}]}}))
            elif method == "tools/call":
                args = req.get("params", {}).get("arguments", {})
                router = AgenticFreightCarbonOffsetRouter()
                out = router.optimize_freight_and_offset(args.get("cargo_details", {}), args.get("carrier_options", []))
                print(json.dumps({"jsonrpc": "2.0", "id": msg_id, "result": {"content": [{"type": "text", "text": json.dumps(out)}]}}))
            else:
                print(json.dumps({"jsonrpc": "2.0", "id": msg_id, "error": {"code": -32601, "message": "Method not found"}}))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"jsonrpc": "2.0", "error": {"code": -32603, "message": str(e)}}))
            sys.stdout.flush()

if __name__ == "__main__":
    main()
