import os
from config import PATH_TO_REPOSITORY


def send_imessage_text(recipient_number, message):
    # Formating message for AppleScript
    message = message.replace("'", "")
    message = "'" + message + "'"

    try:
        path = PATH_TO_REPOSITORY + "/send_message.applescript"

        if not os.path.isfile(path):
            raise FileNotFoundError(f"AppleScript file not found at {path}")

        os.system(f"osascript {path} {recipient_number} {message}")

    except FileNotFoundError as fnfe:
        print(f"FileNotFoundError: {fnfe}")
