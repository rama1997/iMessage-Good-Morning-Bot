from rain_alert import send_rain_alert
from dog_pic import send_dog_pic
from send_message import send_message
from daily_holiday import send_daily_holiday_alert
from config import MORNING_MESSAGE, CLOSING_MESSAGE
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

if __name__ == "__main__":
    # Get the name of profile through command line arguments
    args = ap.parse_args()
    if args:
        try:
            profile = __import__("profiles." + args.name, fromlist=[args.name])
        except ImportError as e:
            print("Failed to import profile:", e)
            profile = ""

    if profile:
        send_message(
            recipient_number=profile.USER_NUMBER,
            message=MORNING_MESSAGE + profile.USER_NAME + " ☀️☀️",
        )
        send_daily_holiday_alert(recipient_number=profile.USER_NUMBER)
        send_dog_pic(recipient_number=profile.USER_NUMBER)
        send_rain_alert(recipient_number=profile.USER_NUMBER, city=profile.CITY)
        send_message(recipient_number=profile.USER_NUMBER, message=CLOSING_MESSAGE)
        print(f"Sent to {profile.USER_NAME}")
