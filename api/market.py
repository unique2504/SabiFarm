CROP_PRICES = {
    "Maize": 200,
    "Cassava": 150,
    "Yam": 300,
    "Rice": 250
}

def market_report(crop_type: str, expected_yield_kg: float):
    price = CROP_PRICES.get(crop_type, 100)
    revenue = expected_yield_kg * price
    return {
        "crop": crop_type,
        "current_price": price,
        "expected_yield_kg": expected_yield_kg,
        "expected_revenue": revenue
    }
