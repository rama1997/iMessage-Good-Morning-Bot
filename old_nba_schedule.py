from datetime import datetime, timezone
from dateutil.parser import parse
from nba_api.live.nba.endpoints import scoreboard
from iMessage import send_imessage_text


def get_todays_game_schedule() -> list[str]:
    """
    Return list of NBA games being played today
    """
    board = scoreboard.ScoreBoard()
    all_games_today = board.games.get_dict()

    schedule = []
    for i, game in enumerate(all_games_today):
        away_team = game["awayTeam"]["teamName"].upper()
        home_team = game["homeTeam"]["teamName"].upper()
        game_title = "{awayTeam} at {homeTeam}".format(
            awayTeam=away_team, homeTeam=home_team
        )

        game_time = parse(game["gameTimeUTC"])
        game_time_localized = game_time.replace(tzinfo=timezone.utc).astimezone(tz=None)

        schedule.append(
            f"Game {i+1}: {game_title} at {game_time_localized.strftime('%I:%M %p')}"
        )

    return schedule


def send_nba_schedule(recipient_number):
    schedule = get_todays_game_schedule()

    if schedule != []:
        message = "Today's NBA game: \n"
        for game in schedule:
            message += "\n" + game + "\n"

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
