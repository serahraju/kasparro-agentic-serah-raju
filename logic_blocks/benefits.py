def generate_benefits(product: dict) -> dict:
    """Generate structured benefits info from product."""
    return {
        "primary_benefits": product.get("benefits"),
        "target_skin_type": product.get("skin_type"),
    }
