from typing import Dict, Any
from .base import Agent

class ProductParserAgent(Agent):
    """Parses raw product JSON-like data into a normalized internal model."""

    def name(self) -> str:
        return "product_parser"

    def can_run(self, state: Dict[str, Any]) -> bool:
        return "raw_product_data" in state and "product" not in state

    def run(self, state: Dict[str, Any]) -> Dict[str, Any]:
        raw = state["raw_product_data"]

        product = {
            "name": raw["Product Name"],
            "concentration": raw["Concentration"],
            "skin_type": raw["Skin Type"],
            "ingredients": raw["Key Ingredients"],
            "benefits": raw["Benefits"],
            "usage": raw["How to Use"],
            "side_effects": raw["Side Effects"],
            "price": raw["Price"],
        }
        state["product"] = product

        # Fictional Product B for comparison
        product_b = {
            "name": "RadianceShield Vitamin C + Niacinamide Serum",
            "concentration": "12% Vitamin C + 5% Niacinamide",
            "skin_type": "Normal, Combination, Dull skin",
            "ingredients": "Vitamin C, Niacinamide, Ceramides",
            "benefits": "Boosts radiance, smooths texture, supports skin barrier",
            "usage": "Use at night on clean, dry skin before moisturizer",
            "side_effects": "Mild purging for acne-prone skin in initial weeks",
            "price": 849,
        }
        state["product_b"] = product_b

        return state
