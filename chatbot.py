# Import required libraries for AI chatbot functionality
import os
import streamlit as st
from groq import Groq  # Groq API for fast LLM inference
from dotenv import load_dotenv  # For loading environment variables

# Load environment variables from .env file (for local development)
load_dotenv()

# Initialize Groq AI client with API key
# Supports both Streamlit secrets (production) and .env file (development)
client = Groq(
    api_key=st.secrets.get("GROQ_API_KEY") or os.environ.get("GROQ_API_KEY"),
)

# System prompt that defines the AI teacher's personality and behavior
# This prompt is sent with every conversation to maintain consistent teaching style
SYSTEM_PROMPT = """You are an English teacher for Portuguese speakers. Follow these rules:
1. Always teach and speak in simple, basic English
2. Use short sentences and common words
3. Be patient, encouraging and friendly like a teacher
4. Help students learn English through conversation
5. Gently correct mistakes and explain grammar when needed
6. Ask questions to keep the conversation going
7. Encourage students to practice more English"""


def send_message(message, message_list):
    """
    Send user message to AI and get teacher response
    
    Args:
        message (str): Current user message
        message_list (list): Complete chat history with timestamps
    
    Returns:
        str: AI teacher response or error message
    """
    # Create message list for API call, starting with system prompt
    # The system prompt defines the AI's role as an English teacher
    full_message_list = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]
    
    # Add all previous messages from chat history
    # Remove timestamps since API doesn't need them
    for msg in message_list:
        clean_msg = {
            "role": msg["role"],
            "content": msg["content"]
        }
        full_message_list.append(clean_msg)
    
    # Add the current user message to the conversation
    full_message_list.append({
        "role": "user",
        "content": message
    })

    try:
        # Send request to Groq API using Llama 3.3 70B model
        # This model is fast and good for conversational AI
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",  # Fast, versatile model
            messages=full_message_list,
            max_tokens=1000,  # Limit response length
            temperature=0.7,  # Balance creativity and consistency
        )
        return response.choices[0].message.content
    except Exception as e:
        # Return user-friendly error message if API call fails
        return f"Sorry, I had a problem connecting to the server. Please try again! 🔄"
    
