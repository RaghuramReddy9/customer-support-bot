#  Customer Support AI Assistant

An AI-powered customer support bot built with **Streamlit** and **Google Gemini 1.5 Flash**, deployed live on **Hugging Face Spaces**.  

This project demonstrates how to build and deploy a real-world GenAI application with a clean UI, chat history, and response controls — exactly the type of system companies use for **customer service automation**.

---

##  Features
- Multi-turn **chat history** (remembers previous Q&A in the session)  
- **Response length control** (Short vs Detailed)  
- Deployed on **Hugging Face Spaces** for instant demo access  
- Built with **Streamlit + Gemini API**  

---

## 🌐 Live Demo
👉 [Try it on Hugging Face Spaces](https://huggingface.co/spaces/RaghuramReddyT/customer-support-bot)  

---

## 📸 Screenshot
![Customer Support AI Assistant Screenshot](assets/demo.png)  
*(replace with your actual screenshot from Hugging Face app UI)*  

---

## Tech Stack
- **Python**
- **Streamlit**
- **Google Generative AI SDK**
- **Hugging Face Spaces**

---

## Project Structure
```
customer-support-bot/
│── app.py # Main Streamlit app
│── requirements.txt # Python dependencies
│── README.md # Documentation
│── .gitignore # Keeps .env and venv private
│── assets/demo.png
```

---

## Running Locally
Clone the repo and run with Streamlit:

```bash
git clone https://github.com/RaghuramReddy9/customer-support-bot.git
cd customer-support-bot
pip install -r requirements.txt
streamlit run app.py

---

Set your API key in a .env file:
`
GEMINI_API_KEY=your_api_key_here
`
```
## License
```
MIT License
```