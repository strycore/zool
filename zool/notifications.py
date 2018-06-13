"""Module for Zool notifications"""
import requests

APP_TOKEN = 'xxxx'
USER_KEY = 'xxxx'


def send_notification(message):
    """Send a notification using Pushover"""
    url = 'https://api.pushover.net/1/messages.json'
    payload = {
        'token': APP_TOKEN,
        'user': USER_KEY,
        'message': message,
    }
    response = requests.post(url, payload)
    if response.status_code >= 400:
        raise RuntimeError("Failed to send notification '%s'" % message)
    return response


if __name__ == '__main__':
    RESPONSE = send_notification('This is a test message')
    print(RESPONSE.status_code)
    print(RESPONSE.headers)
    print(RESPONSE.json())
