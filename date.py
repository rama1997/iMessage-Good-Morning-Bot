import datetime


def get_month() -> str:
    """
    Return today's month
    """

    # Get the current date
    now = datetime.datetime.now()

    # Extract the month from the current date
    month = now.strftime("%B")
    return month


def get_date() -> str:
    """
    Return today's date
    """

    # Get the current date
    now = datetime.datetime.now()

    # Extract date from the current date
    date = now.strftime("%d")
    return date


def get_day() -> str:
    """
    Return day of the week
    """

    # Get the current date
    now = datetime.datetime.now()

    # Extract day from the current date
    day = now.strftime("%A")

    return day
