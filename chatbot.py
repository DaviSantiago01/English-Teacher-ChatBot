import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Groq client with API key (works with both .env and Streamlit secrets)
client = Groq(
    api_key=st.secrets.get("GROQ_API_KEY") or os.environ.get("GROQ_API_KEY"),
)

# System prompt to control chatbot behavior
SYSTEM_PROMPT = """You are an English teacher for Portuguese speakers. Follow these rules:
1. Always teach and speak in simple, basic English
2. Use short sentences and common words
3. Be patient, encouraging and friendly like a teacher
4. Help students learn English through conversation
5. Gently correct mistakes and explain grammar when needed
6. Ask questions to keep the conversation going
7. Encourage students to practice more English"""


# Function to send message and get response from AI
def send_message(message, message_list):
    # Create a new list with system prompt at the beginning
    full_message_list = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]
    
    # Add all previous messages
    full_message_list.extend(message_list)
    
    # Add current user message
    full_message_list.append({
        "role": "user",
        "content": message
    })

    # Get response from Groq API
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=full_message_list,
    )
    
    return response.choices[0].message.content