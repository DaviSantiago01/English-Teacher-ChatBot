# Import required libraries for the English Teacher ChatBot
import streamlit as st
from chatbot import send_message  # Custom module for AI chat functionality
from datetime import datetime     # For message timestamps
from streamlit_mic_recorder import mic_recorder  # Voice recording component
import speech_recognition as sr   # Google Speech Recognition API
import io                        # For handling audio data in memory
import tempfile                  # For temporary file operations (if needed)
import wave                      # For audio file processing
import os                        # For environment variables

# Configure Streamlit page settings
st.set_page_config(
    page_title="English Teacher ChatBot",
    page_icon="🎓",
    layout="centered"
)

def process_audio(audio_data):
    """
    Convert recorded audio to text using Google Speech Recognition
    
    Args:
        audio_data: Audio bytes from mic_recorder component
    
    Returns:
        str: Recognized text in English, or None if recognition fails
    """
    # Check if audio data exists
    if audio_data is None:
        return None
    
    # Extract audio bytes from the dictionary returned by mic_recorder
    # The mic_recorder returns either a dict with 'bytes' key or raw bytes
    if isinstance(audio_data, dict) and 'bytes' in audio_data:
        audio_bytes = audio_data['bytes']
    else:
        audio_bytes = audio_data
    
    # Validate audio bytes exist
    if audio_bytes is None:
        return None
    
    # Initialize Google Speech Recognition
    recognizer = sr.Recognizer()
    
    try:
        # Create BytesIO object to work with audio bytes in memory
        # This avoids creating temporary files on disk
        audio_io = io.BytesIO(audio_bytes)
        
        # Use speech_recognition directly with BytesIO (no temp files needed)
        with sr.AudioFile(audio_io) as source:
            # Adjust for ambient noise to improve recognition accuracy
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            # Record the audio from the source
            audio = recognizer.record(source)
        
        # Convert speech to text using Google's API (English)
        text = recognizer.recognize_google(audio, language='en-US')
        
        return text
        
    except sr.UnknownValueError:
        # Audio was unclear or couldn't be understood
        st.warning("🎤 Could not understand the audio. Please speak more clearly.")
        return None
    except sr.RequestError:
        # Network or API connection error
        st.error("❌ Connection error with recognition service. Check your internet.")
        return None
    except Exception as e:
        # Generic error handling - don't interrupt user experience
        st.info("🎤 There was a problem with the audio. Please try text chat instead.")
        return None

# Main page title and description
st.title("🎓 English Teacher ChatBot")
st.write("Learn English with your AI teacher! Practice conversation in simple English.")

# Sidebar with clear chat functionality
if st.sidebar.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# Initialize chat history in Streamlit session state
# This persists messages during the user session
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show welcome message on first visit (when no messages exist)
if len(st.session_state.messages) == 0:
    with st.chat_message("assistant"):
        st.markdown("Hello! I'm your English teacher. Let's practice English together! 😊")

# Display chat message history FIRST (appears at top/middle of screen)
# This ensures proper chat layout with history above and input below
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        # Show timestamp if available
        if "timestamp" in message:
            st.caption(f"🕐 {message['timestamp']}")

# Voice recording section (positioned above the text input)
# Uses a single column layout for the microphone button
col_audio = st.columns([1])[0]
with col_audio:
    audio_bytes = mic_recorder(
        start_prompt="🎤 Click to record",
        stop_prompt="⏹️ Click to stop",
        just_once=False,  # Allow multiple recordings
        use_container_width=True,
        key="voice_recorder"
    )

# Initialize user message variable
user_message = None

# Process voice input if audio was recorded
if audio_bytes is not None:
    with st.spinner("Processing audio..."):
        audio_text = process_audio(audio_bytes)
        if audio_text:
            user_message = audio_text
            st.success(f"🎤 You said: '{audio_text}'")

# Main text input (Streamlit automatically pins this to the bottom)
if prompt := st.chat_input("Type your message here..."):
    user_message = prompt

# Process any user message (from text or voice input)
if user_message:
    # Validate message is not empty or just whitespace
    if not user_message.strip():
        st.warning("⚠️ Please type a message!")
        st.stop()

    # Add user message to chat history with timestamp
    st.session_state.messages.append({
        "role": "user", 
        "content": user_message,
        "timestamp": datetime.now().strftime("%H:%M")
    })

    # Get AI response from chatbot module and add to history
    response = send_message(user_message, st.session_state.messages.copy())
    st.session_state.messages.append({
        "role": "assistant", 
        "content": response,
        "timestamp": datetime.now().strftime("%H:%M")
    })
    
    # Force page refresh to display the new messages
    st.rerun()
