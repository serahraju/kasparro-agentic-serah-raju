def generate_usage(product: dict) -> dict:
    """Generate structured usage instructions."""
    return {
        "instructions": product.get("usage"),
        "recommended_time": "Morning routine",
        "steps": [
            "Cleanse face",
            "Apply 2-3 drops of serum",
            "Follow with moisturizer",
            "Apply sunscreen",
        ],
    }
