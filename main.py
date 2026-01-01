import json
import os
from orchestrator.pipeline import build_pipeline

def run_pipeline():
    raw_product_data = {
        "Product Name": "GlowBoost Vitamin C Serum",
        "Concentration": "10% Vitamin C",
        "Skin Type": "Oily, Combination",
        "Key Ingredients": "Vitamin C, Hyaluronic Acid",
        "Benefits": "Brightening, Fades dark spots",
        "How to Use": "Apply 2-3 drops in the morning before sunscreen",
        "Side Effects": "Mild tingling for sensitive skin",
        "Price": 699,
    }

    graph = build_pipeline()
    final_state = graph.run({"raw_product_data": raw_product_data})

    pages = final_state["pages"]

    os.makedirs("outputs", exist_ok=True)

    with open("outputs/faq.json", "w") as f:
        json.dump(pages["faq"], f, indent=2)
    with open("outputs/product_page.json", "w") as f:
        json.dump(pages["product"], f, indent=2)
    with open("outputs/comparison_page.json", "w") as f:
        json.dump(pages["comparison"], f, indent=2)

    return pages

if __name__ == "__main__":
    run_pipeline()
