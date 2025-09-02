# 🎓 English Teacher ChatBot

A simple AI-powered English teacher that helps Portuguese speakers learn English through conversation.

## ✨ Features

- 💬 **Text Chat**: Type messages and get responses from your AI English teacher
- 🎤 **Voice Input**: Record your voice and the bot will understand what you said
- 🕐 **Message History**: See all your conversations with timestamps
- 🗑️ **Clear Chat**: Start fresh conversations anytime
- 🎯 **Simple English**: The teacher uses easy words and short sentences
- 📚 **Grammar Help**: Get corrections and explanations when you make mistakes

## 🚀 How to Use

1. **Install Requirements**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set Up API Key**:
   - Get a free API key from [Groq](https://groq.com)
   - Create a `.env` file and add:
     ```
     GROQ_API_KEY=your_api_key_here
     ```

3. **Run the App**:
   ```bash
   streamlit run main.py
   ```

4. **Start Learning**:
   - Type messages or click the 🎤 button to record your voice
   - Practice English conversation with your AI teacher
   - Get help with grammar and pronunciation

## 🛠️ Technology

- **Streamlit**: Web app framework
- **Groq API**: Fast AI responses using Llama 3.3 70B
- **Google Speech Recognition**: Voice-to-text conversion
- **Python**: Main programming language

## 📁 Project Structure

```
├── main.py          # Main Streamlit app with UI and voice processing
├── chatbot.py       # AI chat functionality using Groq API
├── requirements.txt # Python dependencies
└── README.md       # This file
```

## 🎯 Perfect For

- Portuguese speakers learning English
- Beginners who want to practice conversation
- Students who prefer voice interaction
- Anyone wanting to improve English skills

## 🔧 Requirements

- Python 3.8+
- Internet connection (for AI and voice recognition)
- Microphone (optional, for voice input)
- Groq API key (free)

---

**Happy Learning! 📚✨**

*Start your English learning journey today with your personal AI teacher!*
