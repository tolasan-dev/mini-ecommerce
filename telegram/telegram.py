from http.client import responses
import requests

token = "8302158872:AAHc5N1XABVNV0S3JFvZ6CgqBflgdTkSyrQ"
user_agent = "Telegram Bot kimikimiki SU54 Group"

def getMe(token: str):
    url = f"https://api.telegram.org/bot{token}/getMe"
    headers = {
        "accept": "application/json",
        "User-Agent": user_agent
    }
    response = requests.post(url, headers=headers)
    return response.text

def sendMessage(token: str, message: str):
    import requests

    url = f"https://api.telegram.org/bot{token}/sendMessage"

    payload = {
        "text": message,
        "parse_mode": "HTML",
        "chat_id": "@samnamg_channel",
        "disable_web_page_preview": False,
        "disable_notification": False,
        "reply_to_message_id": None
    }
    headers = {
        "accept": "application/json",
        "User-Agent": user_agent,
        "content-type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    return response.text

sendMessage(token=token, message="th from admin")
