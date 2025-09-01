import streamlit as st
from chatbot import send_message

#Page Config
st.set_page_config(
    page_title = "English Teacher ChatBot",
    page_icon="🎓",
    layout = "centered"
)

#Titel
st.title("🎓 English Teacher ChatBot")
st.write("Learn English with your AI teacher! Practice conversation in simple English.")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Type your message here..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get bot response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = send_message(prompt, st.session_state.messages.copy())
            st.markdown(response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})