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
    """Given a city, return True if it will rain in the city today

    Args:
        city (str): City to check weather

    Returns:
        bool: Returns True if it will rain in the city today
    """

    # Call weather API to get daily forecast
    daily_forecasts = call_weather_api(city)

    # determine if it will rain today based on forecast
    for forecast in daily_forecasts["list"]:
        forecast_time = datetime.datetime.fromtimestamp(forecast["dt"])
        if (
            forecast_time.date() == datetime.date.today()
            and forecast["weather"][0]["main"] == "Rain"
        ):
            return True

    return False


def send_rain_alert(recipient_number, city):
    """Given a city, return True if it will rain in the city today

    Args:
        recipient_number (str): Phone number of desired recipient
        city (str): City to check weather
    """

    # Create and send message if it will rain
    if will_rain(city):
        send_message(
            recipient_number=recipient_number,
            message=RAIN_ALERT_MESSAGE.replace("'", ""),
        )
