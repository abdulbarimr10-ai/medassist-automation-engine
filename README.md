# 🚀 MedAssist Automation Engine

A production-style backend automation system that receives incoming data via webhooks, processes it through an API server, stores structured records in a database, and sends real-time alerts for monitoring and reliability.

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
git clone https://github.com/abdulbarimr10-ai/medassist-automation-engine.git
cd medassist-automation-engine

# Create .env file (see below)

docker build -t medassist-engine .
docker run -p 8000:8000 --env-file .env medassist-engine
```

Then open:

```
http://localhost:8000/docs
```

---

## 🔐 Create `.env` file

Create a file named `.env` in the project root:

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

Built as part of hands-on learning in backend systems, automations.
