import requests
import datetime
from iMessage import send_message
from config import OPENWEATHERMAP_API_KEY, RAIN_ALERT_MESSAGE


def call_weather_api(city):
    # Set the API endpoint URL
    url = "https://api.openweathermap.org/data/2.5/forecast"

    # Set the API parameters
    params = {
        "q": city,  # replace with the name of the desired location
        "appid": OPENWEATHERMAP_API_KEY,  # replace with your OpenWeatherMap API key
        "units": "imperial",  # change to 'imperial' for Fahrenheit
    }

    # Send the API request and get the response
    response = requests.get(url, params=params)
    data = response.json()
    return data


def will_rain(city) -> bool:
    daily_forecasts = call_weather_api(city)

    # Check if there is rain in weather forecast
    for forecast in daily_forecasts["list"]:
        forecast_time = datetime.datetime.fromtimestamp(forecast["dt"])
        if (
            forecast_time.date() == datetime.date.today()
            and forecast["weather"][0]["main"] == "Rain"
        ):
            return True

    return False


def send_rain_alert(recipient_number, city):
    if will_rain(city):
        send_message(
            recipient_number=recipient_number,
            message=RAIN_ALERT_MESSAGE.replace("'", ""),
        )
