from fastapi import FastAPI, UploadFile, File
from api import disease_detector, fertilizer, weather, crop_calendar, market,

app = FastAPI(title="FarmSabi API")

@app.post("/disease")
async def disease(file: UploadFile = File(...)):
    return disease_detector.predict_disease(file)

@app.get("/fertilizer")
def fertilizer_endpoint(crop_type: str, land_fertility: float, disease_history: str = ""):
    return fertilizer.recommend_fertilizer(crop_type, land_fertility, disease_history)

@app.get("/weather")
def weather_endpoint(location: str):
    return weather.get_weather(location)

@app.get("/crop_calendar")
def crop_calendar_endpoint(crop_type: str):
    return crop_calendar.crop_calendar(crop_type)

@app.get("/market")
def market_endpoint(crop_type: str, expected_yield_kg: float):
    return market.market_report(crop_type, expected_yield_kg)

from api import irrigation

@app.get("/irrigation")
def irrigation_endpoint(crop_type: str, planting_date: str):
    # For simplicity, generate dummy weather data
    weather_history = [{"rainfall": 0}, {"rainfall": 2}, {"rainfall": 0}, {"rainfall": 1}, {"rainfall": 0}, {"rainfall": 0}, {"rainfall": 0}]
    weather_forecast = [{"rainfall": 0}, {"rainfall": 1}, {"rainfall": 0}]
    return irrigation.irrigation_alert(crop_type, planting_date, weather_history, weather_forecast)


