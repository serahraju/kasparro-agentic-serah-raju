from typing import Dict, Any
from .base import Agent
from logic_blocks.benefits import generate_benefits
from logic_blocks.usage import generate_usage
from logic_blocks.safety import generate_safety
from logic_blocks.comparison import compare_products

class ContentLogicAgent(Agent):
    """Applies reusable logic blocks to generate structured content."""

    def name(self) -> str:
        return "content_logic"

    def can_run(self, state: Dict[str, Any]) -> bool:
        return "product" in state and "content" not in state

    def run(self, state: Dict[str, Any]) -> Dict[str, Any]:
        product = state["product"]
        product_b = state["product_b"]

        content = {
            "benefits": generate_benefits(product),
            "usage": generate_usage(product),
            "safety": generate_safety(product),
        }
        comparison = compare_products(product, product_b)

        state["content"] = content
        state["comparison"] = comparison
        return state
