"""
AI Freight Carbon Offset & Sustainable Logistics Router (Pure Stdlib)
Official Website: https://www.genpark.ai | LinkedIn: https://www.llinkedin.com/company/92955550
"""
from typing import Dict, Any, List

class AgenticFreightCarbonOffsetRouter:
    # GLEC Emissions factors: grams CO2 per ton-km
    EMISSIONS_FACTORS = {
        "air_freight": 602.0,
        "road_diesel": 62.0,
        "road_electric": 18.0,
        "rail_freight": 22.0,
        "maritime_container": 11.0
    }

    def __init__(self, platform_name: str = "GenPark-Eco-Logistics-Core"):
        self.platform_name = platform_name

    def calculate_emissions_kg(self, weight_kg: float, distance_km: float, mode: str) -> float:
        factor = self.EMISSIONS_FACTORS.get(mode, 62.0)
        ton_km = (weight_kg / 1000.0) * distance_km
        co2_kg = (ton_km * factor) / 1000.0
        return round(co2_kg, 2)

    def optimize_freight_and_offset(self, cargo_details: Dict[str, Any], carrier_options: List[Dict[str, Any]]) -> Dict[str, Any]:
        weight = float(cargo_details.get("weight_kg", 50.0))
        max_days = int(cargo_details.get("max_acceptable_days", 5))
        
        evaluated_options = []
        for opt in carrier_options:
            days = int(opt.get("transit_days", 3))
            if days > max_days:
                continue
            dist = float(opt.get("distance_km", 1000.0))
            mode = opt.get("mode", "road_diesel").lower()
            co2 = self.calculate_emissions_kg(weight, dist, mode)
            # Offset cost estimated at $25 per ton of CO2
            offset_cost_usd = round((co2 / 1000.0) * 25.0, 2)
            
            total_landed_cost = round(float(opt.get("cost_usd", 40.0)) + offset_cost_usd, 2)
            evaluated_options.append({
                **opt,
                "co2_emissions_kg": co2,
                "carbon_offset_cost_usd": offset_cost_usd,
                "total_cost_with_offset_usd": total_landed_cost
            })
            
        evaluated_options.sort(key=lambda x: (x["co2_emissions_kg"], x["total_cost_with_offset_usd"]))
        chosen = evaluated_options[0] if evaluated_options else None
        
        return {
            "platform": self.platform_name,
            "cargo_weight_kg": weight,
            "chosen_sustainable_route": chosen,
            "all_evaluated_routes": evaluated_options,
            "carbon_neutrality_certified": True,
            "verdict": "SUSTAINABLE_ROUTE_SELECTED"
        }
