from datetime import datetime, timedelta

# Example crop water needs (mm/day)
CROP_WATER_NEEDS = {
    "Maize": 5,
    "Cassava": 3,
    "Yam": 4,
    "Rice": 6
}

def irrigation_alert(crop_type: str, planting_date: str, weather_history: list, weather_forecast: list):
    """
    crop_type: "Maize", "Cassava", etc.
    planting_date: "YYYY-MM-DD"
    weather_history: list of dicts with past rainfall mm per day
    weather_forecast: list of dicts with predicted rainfall mm per day
    """
    today = datetime.now().date()
    plant_date = datetime.strptime(planting_date, "%Y-%m-%d").date()
    crop_age_days = (today - plant_date).days

    # Water need per day
    daily_need = CROP_WATER_NEEDS.get(crop_type, 4)

    # Calculate total rain in the past week
    past_rain = sum(day.get("rainfall", 0) for day in weather_history[-7:])
    
    # Forecast rain for next 3 days
    forecast_rain = sum(day.get("rainfall", 0) for day in weather_forecast[:3])

    # Simple irrigation logic
    irrigation_required = False
    if past_rain + forecast_rain < daily_need * 3:
        irrigation_required = True

    # Expected harvest date (assume 90 days from planting for simplicity)
    expected_harvest = plant_date + timedelta(days=90)
    
    return {
        "crop": crop_type,
        "crop_age_days": crop_age_days,
        "expected_harvest_date": expected_harvest.strftime("%Y-%m-%d"),
        "irrigation_required": irrigation_required,
        "notes": "Irrigate if soil is dry; monitor rainfall."
    }
