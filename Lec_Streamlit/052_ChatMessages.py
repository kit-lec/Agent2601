import streamlit as st
import time

# Chat elements 
#  공식] https://docs.streamlit.io/develop/api-reference/chat

st.set_page_config(
    page_title="DocumentGPT",
    page_icon="👀",
)

st.title("Chat Messages")

# 챗 입력 위젯 
message = st.chat_input(placeholder="Send a message to AI")

def send_message(message, role):
    with st.chat_message(role):
        st.write(message)

if message:
    send_message(message, 'human')
    time.sleep(2)
    send_message(f'You said: {message}', 'ai')







