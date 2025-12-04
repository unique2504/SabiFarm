# Import FastAPI
from fastapi import FastAPI

# Import all FarmSabi API modules
from api import (
    disease_detector,
    fertilizer,
    weather,
    crop_calendar,
    market,
    irrigation
)

# Initialize FastAPI app
app = FastAPI(title="FarmSabi API", description="Agriculture assistant platform", version="1.0")

# Example endpoint using disease detector
@app.get("/disease")
def disease_endpoint(crop_type: str, image_url: str):
    return disease_detector.predict(crop_type, image_url)

# Example endpoint using fertilizer recommendation
@app.get("/fertilizer")
def fertilizer_endpoint(crop_type: str, soil_fertility: float):
    return fertilizer.recommend(crop_type, soil_fertility)

# Example endpoint for weather information
@app.get("/weather")
def weather_endpoint(location: str):
    return weather.get_weather(location)

# Example endpoint for crop calendar
@app.get("/crop_calendar")
def crop_calendar_endpoint(crop_type: str):
    return crop_calendar.get_calendar(crop_type)

# Example endpoint for market report
@app.get("/market")
def market_endpoint(crop_type: str):
    return market.get_market_info(crop_type)

# Example endpoint for irrigation alert
@app.get("/irrigation")
def irrigation_endpoint(crop_type: str, planting_date: str):
    # For simplicity, using placeholder weather data
    weather_history = [{"rainfall": 0}, {"rainfall": 2}, {"rainfall": 0}, {"rainfall": 1}, {"rainfall": 0}, {"rainfall": 0}, {"rainfall": 0}]
    weather_forecast = [{"rainfall": 0}, {"rainfall": 1}, {"rainfall": 0}]
    return irrigation.irrigation_alert(crop_type, planting_date, weather_history, weather_forecast)
