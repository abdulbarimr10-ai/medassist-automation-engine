# 🚀 MedAssist Automation Engine

A production-style backend automation system that receives incoming data via webhook, processes it through an API server, stores structured records in a database, and sends real-time alerts for monitoring and reliability.

---

## 🧠 The Problem

Healthcare and service teams often depend on **manual data entry** for leads and requests. This leads to:

- Slow response times  
- Human errors  
- Lost opportunities  
- No system failure visibility  

---

## 💡 The Solution

MedAssist Automation Engine is an **end-to-end automated pipeline** that:

- Captures incoming data via webhooks  
- Processes requests using a FastAPI backend  
- Stores structured records in Supabase  
- Sends real-time Telegram alerts  
- Implements retry logic for reliability  
- Runs inside Docker for portable deployment  

The system is built with **resilience, monitoring, and scalability** in mind.

---

## 🏗 System Architecture

```
External Webhook
      ↓
FastAPI Server (Python)
      ↓
Data Processing & Validation
      ↓
Supabase Database
      ↓
Telegram Alerts (Monitoring)
```

---

## 🛠 Tech Stack

| Layer | Technology |
|------|------------|
| Backend API | FastAPI |
| Database | Supabase |
| Monitoring | Telegram Bot Alerts |
| Reliability | Retry Logic + Error Handling |
| Deployment | Docker |
| Language | Python |

---

## ⚙️ Key Features

✔ Webhook-based automation  
✔ Structured data storage  
✔ Real-time failure alerts  
✔ Self-healing retry mechanism  
✔ Dockerized deployment  
✔ Production-style project structure  

---

## 🐳 Run with Docker

```bash
git clone <your-repo-url>
cd medassist-automation-engine
docker build -t medassist-engine .
docker run -p 8000:8000 --env-file .env medassist-engine
```

Then open:

```
http://localhost:8000/docs
```

---

## 🔐 Environment Variables

Create a `.env` file:

```
SUPABASE_URL=your_url
SUPABASE_KEY=your_key
TELEGRAM_TOKEN=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id
```

---

## 📌 Why This Project Matters

This project demonstrates:

- Backend API design  
- Automation pipelines  
- DevOps practices (Docker)  
- System monitoring  
- Error handling & reliability  

It represents a **production-style automation system**, not just a script.

---

## 👨‍💻 Author

Built as part of hands-on learning in backend systems, automation, and DevOps.
