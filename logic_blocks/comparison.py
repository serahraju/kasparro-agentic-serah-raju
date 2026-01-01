def compare_products(product_a: dict, product_b: dict) -> dict:
    """Simple comparison between GlowBoost and fictional Product B."""
    return {
        "product_a": {
            "name": product_a.get("name"),
            "price": product_a.get("price"),
            "benefits": product_a.get("benefits"),
            "skin_type": product_a.get("skin_type"),
        },
        "product_b": {
            "name": product_b.get("name"),
            "price": product_b.get("price"),
            "benefits": product_b.get("benefits"),
            "skin_type": product_b.get("skin_type"),
        },
        "high_level_summary": (
            "GlowBoost focuses on brightening and dark spot reduction, "
            "while Product B offers broader radiance and barrier support."
        ),
    }
