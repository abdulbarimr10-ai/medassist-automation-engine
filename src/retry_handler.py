import time
import requests
from notifier import send_admin_alert

def robust_api_call(url, data, retries=3, delay=5):
    for attempt in range(1, retries + 1):
        try:
            response = requests.post(url, json=data, timeout=10)
            response.raise_for_status()
            return response.json()

        except requests.exceptions.RequestException as e:
            print(f"[Retry {attempt}/{retries}] Error: {e}")

            if attempt < retries:
                time.sleep(delay)
            else:
                send_admin_alert(f"CRITICAL FAILURE: {e}")
                raise