import random
from date import get_month, get_date, get_day

PATH_TO_APPLESCRIPT = "Enter path to send_message.applescript"

OPENWEATHERMAP_API_KEY = "Enter openweathermap API Key"

SPORTSDATA_API_KEY = "Enter sportsdata.io API Key"

REDDIT_API_ID = "Enter Reddit API ID"
REDDIT_API_SECRET = "Enter Reddit API Secret"
REDDIT_USER = "Enter Reddit account username"
REDDIT_PASS = "Enter Reddit account password"

SUBREDDITS = [
    "corgi",
    "dogpictures",
    "puppies",
    "shiba",
    "puppysmiles",
    "lookatmydog",
    "rarepuppers",
]

RAIN_ALERT_MESSAGE = "It is projected to rain today. Stay dry and bring an umbrella. Drive slow and drive safe."

HOLIDAY_MESSAGE = "HAPPY {HOLIDAY}!! 🎉"

DOG_PIC_MESSAGE = (
    "Here's a daily dog picture to start your day off 🤗 \n\nPost Title: {TITLE} \n{URL}"
)

MONTH = get_month()
DAY = get_day()
DATE = get_date()

with open("quotes.txt", "r") as file:
    quotes = file.readlines()

MOTIVATION_QUOTE = random.choice(quotes)

MORNING_GREETING = "Good Morning {NAME} ☀️☀️. Today is {DAY}, {MONTH} {DATE}."

CLOSING_MESSAGE = f"Have a good rest of your day.".replace(
    "'", ""
)
