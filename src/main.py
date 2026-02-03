from fastapi import FastAPI
from src.database import save_lead
from src.notifier import send_admin_alert


app = FastAPI()

@app.post("/webhook")
def receive_data(data: dict):
    try:
        save_lead(data)
        send_admin_alert("New lead saved successfully ✅")
        return {"status": "success"}
    except Exception as e:
        send_admin_alert(f"ERROR: {e}")
        return {"status": "error"}
