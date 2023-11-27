import datetime


def get_month() -> str:
    now = datetime.datetime.now()
    month = now.strftime("%B")
    return month


def get_date() -> str:
    now = datetime.datetime.now()
    date = now.strftime("%-d")
    return date


def get_day() -> str:
    now = datetime.datetime.now()
    day = now.strftime("%A")
    return day
