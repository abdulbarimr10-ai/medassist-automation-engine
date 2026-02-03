import requests
from dotenv import load_dotenv
import os

load_dotenv()


def send_admin_alert(message):
    token=os.getenv("Telegram_Token")
    chat_id=os.getenv("TELEGRAM_CHAT_ID")

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}

    try:
        requests.post(url, data=payload, timeout=5)
    except Exception as e:
        print("Failed to send alert:", e)