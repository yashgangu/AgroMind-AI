# services/weather_service.py
# Replace your ENTIRE file with this code.
# This file contains BOTH:
# 1. get_weather(city)
# 2. get_weather_by_coordinates(latitude, longitude)

import requests


def _fetch_weather(latitude, longitude):
    """
    Internal helper function to fetch weather from Open-Meteo.
    """
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        "&current="
        "temperature_2m,"
        "relative_humidity_2m,"
        "wind_speed_10m,"
        "soil_temperature_0cm,"
        "soil_moisture_0_to_1cm"
        "&daily="
        "precipitation_probability_max,"
        "temperature_2m_max,"
        "temperature_2m_min"
        "&timezone=auto"
    )

    try:
        response = requests.get(url, timeout=10)
        data = response.json()
    except Exception as e:
        return {"error": str(e)}

    if "current" not in data:
        return {"error": "Unable to fetch weather data."}

    current = data["current"]
    daily = data["daily"]

    return {
        "temperature": current["temperature_2m"],
        "humidity": current["relative_humidity_2m"],
        "wind_speed": current["wind_speed_10m"],
        "soil_temperature": current["soil_temperature_0cm"],
        "soil_moisture": current["soil_moisture_0_to_1cm"],
        "rain_probability": daily["precipitation_probability_max"][0],
        "max_temperature": daily["temperature_2m_max"][0],
        "min_temperature": daily["temperature_2m_min"][0],
    }


def get_coordinates(city):
    """
    Convert city name to latitude and longitude.
    """
    url = (
        "https://geocoding-api.open-meteo.com/v1/search"
        f"?name={city}&count=1"
    )

    try:
        response = requests.get(url, timeout=10)
        data = response.json()
    except Exception as e:
        return {"error": str(e)}

    if "results" not in data or len(data["results"]) == 0:
        return {"error": "City not found."}

    result = data["results"][0]

    return {
        "city": result["name"],
        "country": result.get("country", ""),
        "latitude": result["latitude"],
        "longitude": result["longitude"],
    }


def get_weather(city):
    """
    Get weather using city name.
    """
    location = get_coordinates(city)

    if "error" in location:
        return location

    weather = _fetch_weather(
        location["latitude"],
        location["longitude"]
    )

    if "error" in weather:
        return weather

    weather["city"] = location["city"]
    weather["country"] = location["country"]

    return weather


def get_weather_by_coordinates(latitude, longitude):
    """
    Get weather using latitude and longitude.
    """
    return _fetch_weather(latitude, longitude)