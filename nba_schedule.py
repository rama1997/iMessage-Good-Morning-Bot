import requests
from datetime import datetime, timezone
from config import SPORTSDATA_API_KEY
from iMessage import send_imessage_text

def get_todays_game_schedule():
    API_URL = 'https://api.sportsdata.io/v3/nba/scores/json/GamesByDateFinal/'

    today = datetime.today().strftime('%Y-%m-%d')

    url = f"{API_URL}{today}"
    headers = {'Ocp-Apim-Subscription-Key': SPORTSDATA_API_KEY}

    schedule = []

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status() # Check for request errors
        games = response.json()

        if not games:
            return schedule

        for i, game in enumerate(games):
            home_team = game['HomeTeam']
            away_team = game['AwayTeam']
            game_time_utc = game['DateTimeUTC']
            
            # Parse the UTC game time and convert to local time
            game_time_localized = (
                datetime.fromisoformat(game_time_utc)
                .replace(tzinfo=timezone.utc)
                .astimezone(tz=None) # Convert to local timezone directly
            )

            game_time_formatted = game_time_localized.strftime('%I:%M %p')

            channels = game.get('Channel')

            schedule.append([home_team,away_team,game_time_formatted,channels])

    except requests.exceptions.RequestException as e:
        schedule = []

    return schedule


def send_nba_schedule(recipient_number):
    schedule = get_todays_game_schedule()

    if schedule != []:
        message = "Today's NBA game: "
        for i, game in enumerate(schedule):
            home_team = game[0]
            away_team = game[1]
            game_time = game[2]
            channels = game[3]
            message += "\n\n" + f"Game {i+1}: {home_team} at {away_team}" + "\n" + f"Time: {game_time}" + "\n" + f"Channels: {channels}"

        send_imessage_text(
            recipient_number=recipient_number,
            message=message,
        )
    else:
        message = "No NBA games today."
        send_imessage_text(
            recipient_number=recipient_number,
            message=message,
        )
