from typing import Dict, Any, List
from .base import Agent

class TemplateAgent(Agent):
    """Assembles structured pages using templates."""

    def name(self) -> str:
        return "template_builder"

    def can_run(self, state: Dict[str, Any]) -> bool:
        return (
            "product" in state
            and "questions" in state
            and "content" in state
            and "comparison" in state
            and "pages" not in state
        )

    def _build_faq_page(self, questions: Dict[str, List[str]], content: Dict[str, Any]) -> Dict[str, Any]:
        items = []
        for category, qs in questions.items():
            for q in qs:
                if category == "informational":
                    answer = content["benefits"]["primary_benefits"]
                elif category == "usage":
                    answer = content["usage"]["instructions"]
                elif category == "safety":
                    answer = content["safety"]["note"]
                elif category == "purchase":
                    answer = "Refer to product page pricing and usage details."
                else:  # comparison
                    answer = "See comparison page for detailed differences."
                items.append(
                    {
                        "category": category,
                        "question": q,
                        "answer": answer,
                    }
                )
        return {
            "page_type": "FAQ",
            "items": items,
        }

    def _build_product_page(self, product: Dict[str, Any], content: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "page_type": "Product",
            "product_name": product["name"],
            "concentration": product["concentration"],
            "skin_type": product["skin_type"],
            "ingredients": product["ingredients"],
            "benefits": content["benefits"]["primary_benefits"],
            "usage": {
                "instructions": content["usage"]["instructions"],
                "steps": content["usage"]["steps"],
                "recommended_time": content["usage"]["recommended_time"],
            },
            "safety": {
                "side_effects": content["safety"]["side_effects"],
                "note": content["safety"]["note"],
                "warnings": content["safety"]["warnings"],
            },
            "price": product["price"],
        }

    def _build_comparison_page(self, comparison: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "page_type": "Comparison",
            "product_a": comparison["product_a"],
            "product_b": comparison["product_b"],
            "summary": comparison["high_level_summary"],
        }

    def run(self, state: Dict[str, Any]) -> Dict[str, Any]:
        product = state["product"]
        content = state["content"]
        questions = state["questions"]
        comparison = state["comparison"]

        faq_page = self._build_faq_page(questions, content)
        product_page = self._build_product_page(product, content)
        comparison_page = self._build_comparison_page(comparison)

        state["pages"] = {
            "faq": faq_page,
            "product": product_page,
            "comparison": comparison_page,
        }
        return state
