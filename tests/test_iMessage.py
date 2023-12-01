import pytest
from iMessage import send_imessage_text


@pytest.mark.parametrize(
    "recipient_number, message",
    [("", "Hello"), ("1", ""), ("", "")],
)
def test_send_imessage_path_file_not_found(
    recipient_number, message, monkeypatch, capsys
):
    # Mocking the file existence check to simulate file not found
    monkeypatch.setattr("os.path.isfile", lambda x: False)

    send_imessage_text(recipient_number, message)

    # Get the printed output
    captured = capsys.readouterr()

    # Assert that the expected error message is printed
    assert "FileNotFoundError" in captured.out


@pytest.mark.parametrize(
    "recipient_number, message",
    [("", "Hello"), ("1", ""), ("", "")],
)
def test_send_imessage_path_file_found(recipient_number, message, monkeypatch, capsys):
    # Mocking the file existence check to simulate file found
    monkeypatch.setattr("os.path.isfile", lambda x: True)

    send_imessage_text(recipient_number, message)

    # Get the printed output
    captured = capsys.readouterr()

    # Assert that the expected output is printed
    assert "FileNotFoundError" not in captured.out
