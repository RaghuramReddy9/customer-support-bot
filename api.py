from fastapi import FastAPI
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_google_genai import ChatGoogleGenerativeAI

# Load env variables
load_dotenv()

# Explicitly set API key so SDK doesn't fall back to ADC
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env")

# Configure Gemini with LangChain wrapper
llm = ChatGoogleGenerativeAI(
    model= "gemini-1.5-flash",
    temperature=0.2,
    google_api_key=api_key,
    convert_system_message_to_human=True
)

# add memory so bot remembers context of conversation
memory = ConversationBufferMemory(return_messages=True)

# create conversation chain
chain = ConversationChain(llm=llm, memory=memory, verbose=True)

# initializing FastAPI app
app = FastAPI()

# pydantic model for input
class Query(BaseModel):
    question: str

@app.post("/ask")
def ask_bot(query: Query):
    """API endpoint for customer support queries"""
    response = chain.run(query.question)
    return {"answer": response}

@app.get("/history")
def get_history():
    """Return full chat history"""
    return {"history": memory.load_memory_variables({})}
