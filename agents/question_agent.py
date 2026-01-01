from typing import Dict, Any
from .base import Agent

class QuestionGenerationAgent(Agent):
    """Generates categorized user questions based on product data."""

    def name(self) -> str:
        return "question_generation"

    def can_run(self, state: Dict[str, Any]) -> bool:
        return "product" in state and "questions" not in state

    def run(self, state: Dict[str, Any]) -> Dict[str, Any]:
        product = state["product"]
        name = product["name"]

        questions = {
            "informational": [
                f"What is {name}?",
                "What does this serum do?",
                "Who is this serum suitable for?",
                "What are the key benefits of this serum?",
                "What skin concerns does it target?",
            ],
            "usage": [
                "How do I apply this serum?",
                "When should I use it in my routine?",
                "Can it be used daily?",
                "Can I use it with other active ingredients?",
                "How much product should I use each time?",
            ],
            "safety": [
                "Are there any side effects?",
                "Is it safe for sensitive skin?",
                "Should I do a patch test before use?",
                "Can pregnant or breastfeeding women use this?",
                "What should I do if irritation occurs?",
            ],
            "purchase": [
                "What is the price of the serum?",
                "Is it value for money?",
                "How long will one bottle last with regular use?",
                "Is this serum suitable for beginners?",
                "Is it dermatologist tested?",
            ],
            "comparison": [
                "How does it compare to other Vitamin C serums?",
                "What makes it different from alternatives?",
                "Is it better for oily skin than other serums?",
                "How does it compare in price and benefits?",
                "Is it more gentle than higher concentration Vitamin C serums?",
            ],
        }

        state["questions"] = questions
        return state
