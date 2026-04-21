import streamlit as st
import time

st.set_page_config(
    page_title="DocumentGPT",
    page_icon="👀",
)

# ai 와 주고 받은 Chat message 들을 담기 위해
# list 를 사용해 보면?

st.title("Chat Messages")

messages = []  # 매번 실행때 마다 비어있는 list 로 시작하게 된다.

message = st.chat_input(placeholder="Send a message to AI")

def send_message(message, role):
    with st.chat_message(role):
        st.write(message)
        messages.append({'messages': message, 'role': role})
    st.write(messages)  # 확인용.        

if message:
    send_message(message, 'human')
    time.sleep(2)
    send_message(f'You said: {message}', 'ai')

# 다시 재실행되어도 기존의 입려한 chat message 들이 남아 있어야 된다! 어떻게?






