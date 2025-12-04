import requests

API_KEY = "your_openweathermap_api_key"  # Replace with real key

def get_weather(location: str):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
    response = requests.get(url).json()
    return {
        "location": location,
        "temperature": response.get("main", {}).get("temp"),
        "humidity": response.get("main", {}).get("humidity"),
        "rainfall": response.get("rain", {}).get("1h", 0)
    }
