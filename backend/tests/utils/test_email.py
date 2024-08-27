import pytest
from unittest.mock import patch
from src.utils.email import send_email


@pytest.fixture
def mock_smtp():
    with patch("smtplib.SMTP") as mock:
        yield mock

def test_send_email_success(mock_smtp):
    mock_instance = mock_smtp.return_value
    mock_instance.sendmail.return_value = None

    message = "Hello, this is a test email."
    to_whom = "recipient@example.com"

    result = send_email(message, to_whom)
    
    assert result == "The message was sent successfully!"
    mock_instance.starttls.assert_called_once()
    mock_instance.login.assert_called_once_with("seamusic.official@yandex.com", "unsp777.")
    mock_instance.sendmail.assert_called_once()

def test_send_email_failure(mock_smtp):
    mock_instance = mock_smtp.return_value
    mock_instance.sendmail.side_effect = Exception("Failed to send email.")
    
    message = "Hello, this is a test email."
    to_whom = "recipient@example.com"
    
    result = send_email(message, to_whom)
    
    assert "Failed to send email." in result
    mock_instance.starttls.assert_called_once()
    mock_instance.login.assert_called_once_with("seamusic.official@yandex.com", "unsp777.")
    mock_instance.sendmail.assert_called_once()