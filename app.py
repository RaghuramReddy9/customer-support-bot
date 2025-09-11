import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()

# Get key from env (local .env or HF secrets)
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Load model
model = genai.GenerativeModel("gemini-1.5-flash")

# Streamlit app
st.set_page_config(page_title="Customer Support AI Assistant", page_icon="💬")

st.title("💬 Customer Support AI Assistant")
st.write("Ask me any customer support question!")

# initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Add response length option
length = st.selectbox("Choose response style:", ["Short (3–4 sentences)", "Detailed (full answer)"])

# User input
user_input = st.text_input("Your question:")

if st.button("Get Answer"):
    if user_input.strip():
        with st.spinner("Thinking..."):
            if "short" in length:
                instruction = "Answer clearly in 3-4 sentences."
            else:
                instruction = "Provide a detailed and helpful answer."
               
            response = model.generate_content(user_input)
            answer = response.text
            
            # save chat history
            st.session_state.chat_history.append({"user": user_input, "bot": answer})
    
# Display chat history
if st.session_state.chat_history:
    st.subheader("Conversation History")
    for i, chat in enumerate(st.session_state.chat_history, 1):
        st.markdown(f"**You:** {chat['user']}")
        st.markdown(f"**Bot:** {chat['bot']}")
        st.markdown("---")