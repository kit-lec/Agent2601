import streamlit as st
import time

st.set_page_config(
    page_title="DocumentGPT",
    page_icon="👀",
)

st.title("Chat Messages")

# refresh 되더라도 상태값을 기억하도록
# streamlit 에서는 session state 제공.
# session state 는 여러번 재실행해도 data 가 보존될수 있도록 해준다.

# session_state 는 여러번 재실행해도 data 가 보존될수 있도록 해준다.
#   보존되는 데이터는 key-value 형태로 session에 저장됨

# session_state 의 'messages' 라는 key 에 담아볼거다.
# 명심! 언제든지 refresh 될때 재실행 된다는 사실 있지 말자
# ↓ session_state 가 messages 라는 key 값이 없는 경우에만 빈 list 로 초기화
#    이기 가지고 있었다면 (즉, 이미 값이 있었따면) 아무것도 하지 않는다.

if 'messages' not in st.session_state:
    st.session_state['messages'] = []

st.write(st.session_state['messages']) # 확인용

def send_message(message, role):
    with st.chat_message(role):
        st.write(message)
        st.session_state['messages'].append({'message': message, 'role': role})
    
message = st.chat_input(placeholder="Send a message to AI")

if message:
    send_message(message, 'human')
    time.sleep(2)
    send_message(f'You said: {message}', 'ai')







