import streamlit as st
import time

st.set_page_config(
    page_title="DocumentGPT",
    page_icon="👀",
)

st.title("Chat Messages")

# session_state 에 있는 messages 들을 그리기.

if 'messages' not in st.session_state:
    st.session_state['messages'] = []

def send_message(message, role, save=True):
    with st.chat_message(role):
        st.write(message)
    if save:
        st.session_state['messages'].append({'message': message, 'role': role})


# 챗 히스토리 화면에 그리기
# session_state['messages'] 이 있다면 send_message() 호출하여 그리기
# 화면에 그림만 그릴때는 session 에 저장하면 안되기에 save=False 로 호출
for msg in st.session_state['messages']:
    send_message(msg['message'], msg['role'], save=False)

message = st.chat_input(placeholder="Send a message to AI")

if message:
    send_message(message, 'human') # save=True  -> session 에 저장.
    time.sleep(2)
    send_message(f'You said: {message}', 'ai')

    # 
    with st.sidebar:
        st.write(st.session_state['messages'])







