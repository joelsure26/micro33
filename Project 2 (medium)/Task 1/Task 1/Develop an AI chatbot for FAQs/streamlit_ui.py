import streamlit as st
from app import get_response

st.set_page_config(page_title="Conversational FAQ Chatbot 🤖", page_icon="💬")

st.title("📚 Internship & Application Conversational Chatbot")

# Initialize conversation memory
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! 👋 I'm your FAQ bot. How can I help you today?"}
    ]

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input box
user_input = st.chat_input("Type your question here...")

if user_input:
    # Append user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get bot response
    response, intent = get_response(user_input)
    st.session_state.messages.append({"role": "assistant", "content": response})

    # Display bot response
    with st.chat_message("assistant"):
        st.markdown(response)
