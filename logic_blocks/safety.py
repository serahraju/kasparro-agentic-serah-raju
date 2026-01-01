def generate_safety(product: dict) -> dict:
    """Generate structured safety / side-effect info."""
    return {
        "side_effects": product.get("side_effects"),
        "note": "Patch test recommended for sensitive skin",
        "warnings": [
            "Avoid contact with eyes",
            "Do not apply on broken skin",
            "Introduce gradually if you have sensitive skin",
        ],
    }
