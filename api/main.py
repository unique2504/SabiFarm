from fastapi import FastAPI, UploadFile, File
from api import disease_detector, fertilizer, weather, crop_calendar, market, irrigation

app = FastAPI(
    title="FarmSabi API",
    description="Agriculture assistant platform with disease detection, fertilizer recommendation, weather info, crop calendar, market data, and irrigation alerts.",
    version="1.0"
)

# -------------------------------
# Disease Detection Endpoint
# -------------------------------
@app.post("/disease")
async def disease(file: UploadFile = File(...)):
    """
    Upload an image of the crop to detect disease.
    """
    contents = await file.read()
    return disease_detector.predict_disease(contents)


# -------------------------------
# Fertilizer Recommendation Endpoint
# -------------------------------
@app.get("/fertilizer")
def fertilizer_endpoint(crop_type: str, soil_fertility: float):
    """
    Get fertilizer recommendation based on crop type and soil fertility.
    """
    return fertilizer.recommend(crop_type, soil_fertility)


# -------------------------------
# Weather Information Endpoint
# -------------------------------
@app.get("/weather")
def weather_endpoint(location: str):
    """
    Get current weather info for the specified location.
    """
    return weather.get_weather(location)


# -------------------------------
# Crop Calendar Endpoint
# -------------------------------
@app.get("/crop_calendar")
def crop_calendar_endpoint(crop_type: str):
    """
    Get crop calendar for a specific crop type.
    """
    return crop_calendar.get_calendar(crop_type)


# -------------------------------
# Market Report Endpoint
# -------------------------------
@app.get("/market")
def market_endpoint(crop_type: str):
    """
    Get market data and pricing info for a specific crop.
    """
    return market.get_market_info(crop_type)


# -------------------------------
# Irrigation Alert Endpoint
# -------------------------------
@app.get("/irrigation")
def irrigation_endpoint(crop_type: str, planting_date: str):
    """
    Get irrigation alert based on crop type, planting date,
    weather history, and forecast.
    """
    # Placeholder weather data — replace with real API later
    weather_history = [
        {"rainfall": 0}, {"rainfall": 2}, {"rainfall": 0},
        {"rainfall": 1}, {"rainfall": 0}, {"rainfall": 0}, {"rainfall": 0}
    ]
    weather_forecast = [{"rainfall": 0}, {"rainfall": 1}, {"rainfall": 0}]
    
    return irrigation.irrigation_alert(crop_type, planting_date, weather_history, weather_forecast)
