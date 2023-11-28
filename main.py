from rain_alert import send_rain_alert
from dog_pic import send_dog_pic
from iMessage import send_imessage_text
from daily_holiday import send_daily_holiday_alert
from nba_schedule import send_nba_schedule
from config import (
    MORNING_GREETING,
    CLOSING_MESSAGE,
    MONTH,
    DATE,
    DAY,
    MOTIVATION_QUOTE_MESSAGE,
)
import argparse

# Create an argument parser
ap = argparse.ArgumentParser()

# Add arguments and options to the parser
ap.add_argument(
    "-n",
    "--name",
    required=True,
    type=str,
    help="name of profile to send message to",
)


def send_good_morning_messages(profile):
    user_name = profile.USER_NAME
    user_number = profile.USER_NUMBER
    user_city = profile.CITY

    if profile.MORNING_GREETING == True:
        send_imessage_text(
            recipient_number=user_number,
            message=MORNING_GREETING.format(
                NAME=user_name, DAY=DAY, MONTH=MONTH, DATE=DATE
            ).replace("'", ""),
        )
    if profile.HOLIDAY_ALERT == True:
        send_daily_holiday_alert(recipient_number=user_number)
    if profile.DOG_PIC == True:
        send_dog_pic(recipient_number=user_number)
    if profile.RAIN_ALERT == True:
        send_rain_alert(recipient_number=user_number, city=user_city)
    if profile.NBA_SCHEDULE == True:
        send_nba_schedule(recipient_number=user_number)
    if profile.MOTIVATIONAL_QUOTE == True:
        send_imessage_text(
            recipient_number=user_number, message=MOTIVATION_QUOTE_MESSAGE
        )
    if profile.CLOSING_MESSAGE == True:
        send_imessage_text(recipient_number=user_number, message=CLOSING_MESSAGE)


if __name__ == "__main__":
    # Get the name of profile through command line arguments
    args = ap.parse_args()
    if args:
        try:
            profile = __import__("profiles." + args.name, fromlist=[args.name])
        except ImportError as e:
            print("Failed to import profile:", e)
            profile = ""

    # If profile is found, send custom messages
    if profile:
        send_good_morning_messages(profile)
