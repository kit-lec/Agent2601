import streamlit as st
import time

# Chat elements 
#  공식] https://docs.streamlit.io/develop/api-reference/chat

st.set_page_config(
    page_title="DocumentGPT",
    page_icon="👀",
)

st.title("Chat Messages")

# chat_message()  : chat message container 생성
#             human 혹은 AI 모두에게서 받을수 있다.
#     매개변수는 'user', 'assistant', 'ai', 'human' 중 하나
with st.chat_message(name='human'):
    st.write('hello')
    st.write('how are you?')

with st.chat_message(name='ai'):
    st.write('nice to meet you!')    

# 챗 입력 위젯 
st.chat_input(placeholder="Send a message to AI")

# --------------------------------------------------
# status : Insert a status container to display output from long-running tasks.
#  시간이 오래걸리는 작업에 대해서 진행 status(상태) 표시 위젯

# with st.status("Embedding file..."):
#     time.sleep(3)
#     st.write("Getting the file")
#     time.sleep(3)
#     st.write("Embedding the file")
#     time.sleep(3)
#     st.write("Caching the file")

# with st.status("Embedding file...", expanded=True):
#     time.sleep(3)
#     st.write("Getting the file")
#     time.sleep(3)
#     st.write("Embedding the file")
#     time.sleep(3)
#     st.write("Caching the file")

# status 업데이트도 가능!
with st.status("Embedding file...", expanded=True) as status:
    time.sleep(3)
    st.write("Getting the file")
    time.sleep(3)
    st.write("Embedding the file")
    time.sleep(3)
    st.write("Caching the file")

    # state= : 'running' 'complete' 'error' 값 설정 가능.
    status.update(label="Error", state='error')






