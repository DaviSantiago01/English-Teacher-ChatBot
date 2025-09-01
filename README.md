# ChatBot Simples

*My first repository 100% in English*

A simple chatbot built with Python using the Groq API and Llama 3.3 model.

## Description

This is a basic chatbot that uses Groq's AI service to have conversations with users. The bot keeps track of conversation history and provides responses using the Llama 3.3 70B model.

## Features

- Interactive chat in the terminal
- Conversation memory (remembers previous messages)
- Uses Groq's fast AI API
- Simple and clean code structure

## Requirements

- Python 3.7+
- Groq API key
- Required packages (see requirements.txt)

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd ChatBot-Simples
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file and add your Groq API key:
```
GROQ_API_KEY=your_api_key_here
```

## How to Use

1. Run the chatbot:
```bash
python chatbot.py
```

2. Type your message and press Enter
3. The AI will respond to your message
4. Type "exit" to stop the chatbot

## Getting Your API Key

1. Go to [console.groq.com](https://console.groq.com)
2. Create an account or sign in
3. Go to "API Keys"
4. Create a new API key
5. Copy it to your `.env` file

## Example

```
Type your message: Hello, how are you?
Answer: Hello! I'm doing well, thank you for asking. How are you doing today?

Type your message: What can you help me with?
Answer: I can help you with many things like answering questions, having conversations, explaining topics, and much more. What would you like to talk about?

Type your message: exit
```

## Project Structure

```
ChatBot Simples/
├── chatbot.py          # Main chatbot code
├── main.py            # Empty file for future features
├── requirements.txt   # Python dependencies
├── .env              # Environment variables (not in git)
├── .gitignore        # Git ignore file
└── README.md         # This file
```

## Notes

- Keep your API key secret and never share it
- The chatbot needs internet connection to work
- Conversation history is only saved during the current session

## Future Improvements

- Save conversation history to file
- Add more AI models to choose from
- Create a web interface
- Add more features and commands

---

Made with ❤️ and Python
