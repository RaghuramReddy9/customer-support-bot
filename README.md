#  Customer Support Bot

A **FastAPI + Gemini 1.5 Flash** powered customer support assistant that can answer FAQs and keep track of conversation history.  
The project is containerized with **Docker** and deployed live on **Hugging Face Spaces**.  

---

##  Live Demo
👉 [Customer Support Bot – Hugging Face Spaces](https://raghuramreddyt-customer-support.hf.space/docs)

---

##  Problem Statement
Customer support teams spend huge amounts of time answering repetitive queries.  
This project demonstrates how **LLMs + APIs** can automate FAQ handling while still allowing escalation for complex issues.  

---

##  Features
- **FastAPI backend** exposing `/ask` and `/history` endpoints  
- **LangChain Conversation Memory** (remembers past interactions in a session)  
- **Gemini 1.5 Flash** for fast and cost-efficient LLM responses  
- **Dockerized** for easy deployment anywhere  
- Deployed to **Hugging Face Spaces (Docker mode)**  

---

##  Tech Stack
- **Backend**: FastAPI, Uvicorn  
- **LLM Framework**: LangChain + Gemini 1.5 Flash  
- **Deployment**: Docker, Hugging Face Spaces  
- **Language**: Python 3.10+  

---

## Getting Started (Local)
Clone the repo:
```bash
git clone https://github.com/RaghuramReddy9/customer-support-bot.git
cd customer-support-bot
```
### Install dependencies
```bash
pip install -r requirements.txt
```
### Run FastAPI locally
```bash
uvicorn api:app --reload
```
### API docs available at
```bash
http://127.0.0.1:8000/docs
```
### Docker Run (Local)
```bash
docker build -t customer-support-bot .
```
### Run the container
```bash
docker run -d -p 8000:8000 --env-file .env customer-support-bot
```
### Environment Variables
```bash
GEMINI_API_KEY=your_api_key_here
```

---

## 📜 License
```bash
MIT License. Free to use and modify.
```
## 👨‍💻 Author
```bash
Raghuramreddy Thirumalareddy
```

