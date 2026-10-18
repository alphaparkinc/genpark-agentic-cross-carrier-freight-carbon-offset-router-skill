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
