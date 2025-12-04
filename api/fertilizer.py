def recommend_fertilizer(crop_type: str, land_fertility: float, disease_history: str):
    # Simple rule-based recommendation
    base_n = 50
    base_p = 30
    base_k = 20

    # Adjust based on fertility
    factor = 1 - (land_fertility / 100)
    n = round(base_n * factor)
    p = round(base_p * factor)
    k = round(base_k * factor)

    return {
        "crop": crop_type,
        "N": n,
        "P": p,
        "K": k,
        "notes": f"Adjust based on previous diseases: {disease_history}"
    }
