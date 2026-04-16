import streamlit as st
import os
import time

import numpy as np

from dotenv import load_dotenv
load_dotenv()


print(f'✅ {os.path.basename(__file__)} 실행됨 {time.strftime('%Y-%m-%d %H:%M:%S')}')
print(f'\tOPENAI_API_KEY={os.getenv("OPENAI_API_KEY")[:20]}...')

st.title('layout')

# layout
#  streamlit 에서 제공하는 다양한 레이아웃 
#  공식: https://docs.streamlit.io/develop/api-reference/layout  (◀ 함 보자!)


# 레이아웃 사용방식
# 방식1
cont = st.container(border=True)
cont.write('Container 내부의 element')
cont.markdown('Container 내부의 markdown')

st.write('container 바깥의 element')

cont.write('이건 어디에?')

# 방식2 (추천) with 사용
with st.container(border=True):
    st.write('컨테이너 안 입니다')
    st.bar_chart(np.random.randn(50,3))


# container vs. empty
# container() : 여러 요소들을 담는다
# empty() : 한개의 요소만 담는다.


with st.empty():
    st.write('고릴라')
    st.write('호랑이')


st.title('sidebar')

with st.sidebar:
    st.title('sidebar title')
    st.text_input("BBB")
    st.write("Hello")

# ────────────────────────────────────────────────────────
# tab 
#   공식: https://docs.streamlit.io/develop/api-reference/layout/st.tabs
# st.tabs(["A", "B", "C"])
# ↑ (확인!) 
#   탭 컨트롤 표시된다.

#  선택한 tab 값을 받아올수 있고 이를 사용하여 tab 화면을 그릴수 도 있다.
#  (위의 tabs 는 주석 처리)
st.title("tabs")

tab_one, tab_two, tab_three = st.tabs(['두부', '김치', '라면'])

with tab_one:
    st.subheader('alpha')

with tab_two:
    st.subheader('bravo')

with tab_three:
    st.subheader('charlie')

# ────────────────────────────────────────────────────────
# column 으로 영역을 나누어 표기한 경우
# '반응형' 으로 동작하다
#  공식: https://docs.streamlit.io/develop/api-reference/layout/st.columns
st.title('columns')

col1, col2, col3 = st.columns(3)

with col1:
    st.metric('달러USD', value='1,470 원', delta='-12.00 원')
with col2:
    st.metric('달러USD', value='1,470 원', delta='-12.00 원')
with col3:
    st.metric('달러USD', value='1,470 원', delta='-12.00 원')
