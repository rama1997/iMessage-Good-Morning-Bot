import pytest
from nba_schedule import get_todays_game_schedule


@pytest.fixture
def mock_scoreboard(mocker):
    return mocker.patch("nba_schedule.scoreboard.ScoreBoard")


def test_get_todays_game_schedule(mock_scoreboard):
    # Mock the games dictionary with sample data
    mock_games_dict = [
        {
            "awayTeam": {"teamName": "AwayTeam1"},
            "homeTeam": {"teamName": "HomeTeam1"},
            "gameTimeUTC": "2023-12-01T18:00:00Z",
        },
        {
            "awayTeam": {"teamName": "AwayTeam2"},
            "homeTeam": {"teamName": "HomeTeam2"},
            "gameTimeUTC": "2023-12-01T20:00:00Z",
        },
    ]

    mock_scoreboard.return_value.games.get_dict.return_value = mock_games_dict

    # Call the function
    result = get_todays_game_schedule()

    # Assert the expected result based on the mock data
    expected_result = [
        "Game 1: AWAYTEAM1 at HOMETEAM1 at 10:00 AM",
        "Game 2: AWAYTEAM2 at HOMETEAM2 at 12:00 PM",
    ]
    assert result == expected_result
