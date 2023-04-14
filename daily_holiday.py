import requests
from bs4 import BeautifulSoup
import datetime
from send_message import send_message


def get_today_month_and_date() -> tuple[str, str]:
    """
    Return today's month and date
    """

    # Get the current date
    now = datetime.datetime.now()

    # Extract the month and date from the current date
    month = now.strftime("%B")  # Full month name
    date = now.strftime("%d")  # Day of the month with leading zero

    return month, date


def get_daily_holiday() -> str:
    """
    Given a month and a day, web scrapes 'https://nationaltoday.com' to get most popular holiday of the day
    """

    # Get today's month and date
    month, date = get_today_month_and_date()

    # URL of the page we want to scrape
    url = f"https://nationaltoday.com/{month.lower()}-{date}-holidays/"

    # Send a GET request to the URL and store the response
    html_text = requests.get(url)

    # Parse the HTML content of the page
    soup = BeautifulSoup(html_text.content, "lxml")

    # Find all the holiday card from webpage on the given day
    holiday_cards = soup.find_all("div", class_="day-card")

    holidays = []
    for card in holiday_cards:
        holiday_name = card.h3.text

        # Get thrending share count text for each holiday and turns the count into an integer
        shares_count = card.find("div", class_="trending-share-count")
        if shares_count:
            shares = int(shares_count.text.replace("K", "000").split()[0])
        else:
            shares = 0

        # Store (shares,holidays) in a list
        holidays.append((shares, holiday_name))

    # Sort all holidays based on the share count
    holidays.sort(reverse=True)

    # Return the holiday with the highest share count
    return holidays[0][1]


def get_daily_holiday_backup_website() -> str:
    """
    Webscrapes `https://nationaldaycalendar.com` and return a daily holday. The holiday list on site is not static and changes on each refresh.
    """

    # URL of the page we want to scrape
    url = "https://nationaldaycalendar.com/what-day-is-it/"

    # Send a GET request to the URL and store the response
    html_text = requests.get(url)

    # Parse the HTML content of the page
    soup = BeautifulSoup(html_text.content, "lxml")

    # Finds and obtain the first listed holiday on the site
    first_holiday_block = soup.find("h3", class_="ultp-block-title")
    if first_holiday_block:
        holiday = first_holiday_block.find("a").text.split("–")[0]
        return holiday
    else:
        return ""


def send_daily_holiday_alert(recipient_number):
    holiday = get_daily_holiday()
    message = f"HAPPY {holiday.upper()}!! 🎉🎉".replace("'", "")
    send_message(recipient_number=recipient_number, message=message)
