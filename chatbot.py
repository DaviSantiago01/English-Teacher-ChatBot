import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Groq client with API key
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

# Function to send message and get response from AI
def send_message(message, message_list):
    # Add user message to conversation history
    message_list.append({
        "role": "user",
        "content": message
    })

    # Get response from Groq API
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=message_list,
    )
    
    return response.choices[0].message.content

# Store conversation history
message_list = []

# Main chat loop
while True:
    user_input = input("Type your message: ")
    
    # Exit condition
    if user_input == "exit":
        break
        
    # Get AI response
    answer = send_message(user_input, message_list)
    
    # Add AI response to conversation history
    message_list.append({
        "role": "assistant",
        "content": answer
    })
    
    print("Answer:", answer)


