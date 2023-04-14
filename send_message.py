import os
from config import PATH_TO_APPLESCRIPT


def send_message(recipient_number, message):
    message = "'" + message + "'"
    os.system(f"osascript {PATH_TO_APPLESCRIPT} {recipient_number} {message}")
