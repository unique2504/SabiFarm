from datetime import datetime, timedelta

def crop_calendar(crop_type: str):
    # Simple example based on crop type
    today = datetime.now()
    planting_date = today + timedelta(days=3)
    harvest_date = planting_date + timedelta(days=90)

    return {
        "crop": crop_type,
        "best_planting_date": planting_date.strftime("%Y-%m-%d"),
        "expected_harvest_date": harvest_date.strftime("%Y-%m-%d")
    }
