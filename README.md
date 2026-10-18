# genpark-agentic-cross-carrier-freight-carbon-offset-router-skill

[![Official Hub](https://img.shields.io/badge/GenPark-Official%20Hub-6366f1?style=for-the-badge&logo=compass&logoColor=white)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/company/92955550)
[![Zero External Dependencies](https://img.shields.io/badge/Dependencies-Zero%20(Pure%20Stdlib)-success?style=for-the-badge)](https://www.genpark.ai)
[![MCP Compliant](https://img.shields.io/badge/MCP-JSON--RPC%202.0-blue?style=for-the-badge)](https://www.genpark.ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

> **Official Website**: [https://www.genpark.ai](https://www.genpark.ai)  
> **LinkedIn**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550) ([https://www.llinkedin.com/company/92955550](https://www.llinkedin.com/company/92955550))

AI Cross-Carrier Freight Carbon Offset & Sustainable Logistics Router. Applies GLEC framework emissions factors (air, rail, maritime, electric ground), optimizes multi-carrier shipping routes, and generates verified carbon offset credit allocation certificates.

---

## 🌐 Official GenPark AI Ecosystem Links

- **GenPark Official Website**: [https://www.genpark.ai](https://www.genpark.ai)
- **LinkedIn Official Page**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550) ([https://www.llinkedin.com/company/92955550](https://www.llinkedin.com/company/92955550))

---

## 🌟 Key Features

- **100% Zero External Dependencies**: Runs entirely on the Python 3.9+ standard library.
- **Model Context Protocol (MCP) Standard**: Native support for JSON-RPC 2.0 `initialize`, `tools/list`, and `tools/call`.
- **Industrial-Grade Determinism**: Rigorous exception isolation, predictable algorithmic complexity, and type annotations.
- **Dual Deployment Ecosystem**: Verified across `alphaparkinc` and `Alpha-Park` organizations with multi-account validation.

---

## 🚀 Quick Start

### 1. Direct Python SDK Usage

```python
from client import AgenticFreightCarbonOffsetRouter

def main():
    router = AgenticFreightCarbonOffsetRouter()
    cargo = {"weight_kg": 250.0, "max_acceptable_days": 5}
    routes = [
        {"carrier": "Standard Express Air", "mode": "air_freight", "transit_days": 2, "cost_usd": 320.0, "distance_km": 1500.0},
        {"carrier": "Green Electric Road Line", "mode": "road_electric", "transit_days": 4, "cost_usd": 140.0, "distance_km": 1500.0}
    ]
    res = router.optimize_freight_and_offset(cargo, routes)
    best = res['chosen_sustainable_route']
    print("--- Sustainable Freight Route Optimization ---")
    print(f"Selected: {best['carrier']} ({best['mode']})")
    print(f"Transit: {best['transit_days']} days | Landed Cost: ${best['total_cost_with_offset_usd']}")
    print(f"CO2 Footprint: {best['co2_emissions_kg']} kg (Offset Cost: ${best['carbon_offset_cost_usd']})")

if __name__ == "__main__":
    main()

```

### 2. Run as Model Context Protocol (MCP) Server

Start standard JSON-RPC 2.0 server over `stdio`:

```bash
python mcp_server.py
```

Execute embedded test harness:

```bash
python mcp_server.py --test
```

---

## 🛠️ MCP Tool Specification

Inspect [`skill.json`](skill.json) for parameter schemas and tool definitions compatible with Anthropic Claude, Meta Muse, and OpenAI Function Calling formats.

---

## 📜 License & Community

Licensed under the [MIT License](LICENSE). Copyright © 2026 [GenPark AI](https://www.genpark.ai).
Follow us on LinkedIn: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550) | [https://www.llinkedin.com/company/92955550](https://www.llinkedin.com/company/92955550)
