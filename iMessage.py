import os
from config import PATH_TO_REPOSITORY


def send_message(recipient_number, message):
    message = "'" + message + "'"
    path = PATH_TO_REPOSITORY + "/send_message.applescript"
    os.system(f"osascript {path} {recipient_number} {message}")


def send_picture(recipient_number):
    path = PATH_TO_REPOSITORY + "/send_picture.applescript"
    os.system(f"osascript {path} {recipient_number}")
