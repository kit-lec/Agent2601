import streamlit as st
import numpy as np
import pandas as pd

import os
import time

from dotenv import load_dotenv
load_dotenv()

print(f'✅ {os.path.basename( __file__ )} 실행됨 {time.strftime('%Y-%m-%d %H:%M:%S')}')  # 실행파일명, 현재시간출력
print(f'\tOPENAI_API_KEY={os.getenv("OPENAI_API_KEY")[:20]}...') # 필요한 환경변수


# 서버 실행
# > streamlit run ******.py
#    ※ 초반에 email 물어보면 걍 엔터 치세요.

# 서버 종료
# 터미널창에서 user break (CTRL + C) 연타
# user break 되지 않으면 terminal 종료(kill) 하세요

# 기본적인 widget(ui)

# 타이틀 적용 예시
st.title('기본 출력')

st.title('스마일:sunglasses:')

st.header('헤더를 입력할수 있어요! :sparkles:')
st.subheader('이것은 subheader 입니다')

st.text('일반적인 텍스트')
st.caption('캡션을 넣을수 있습니다')

sample_code = '''
def function():
    print('hello, world')
'''
st.code(sample_code)

st.markdown('streamlit 은 **마크다운 문법을 지원** 합니다')

st.markdown("텍스트의 색상을 :green[초록색]으로, 그리고 **:blue[파란색]** 볼드체로 설정할 수 있습니다.")
st.markdown(r"$\sqrt{x^2+y^2}=1$ latex 문법 수식표현")

st.latex(r"\sqrt{x^2+y^2}=1")

st.markdown("---")

st.title("Dataframe, Metric")

# DataFrame 생성
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
})

st.dataframe(df, use_container_width=True)

st.table(df)

st.metric(label="온도", value="10도", delta="1.2도")
st.metric(label="삼성전자", value="161,000원", delta="-23,000원")

st.markdown('---')

st.title('write()')

st.write('hello')
st.write(10, 20, 30)

st.write([1, 2, 3, 4])
st.write({"x": 100, "y": 200})

import re
st.write(re)
st.write(re.Pattern)

# Streamlit 의 magic?
[100, 200, 300, 400]

4 * 700

st.markdown('---')
st.title('Chart 그리기')

import matplotlib.pyplot as plt
import seaborn as sns

# 한글폰트 설정
from matplotlib import font_manager, rc
import platform
try : 
    if platform.system() == 'Windows':
    # 윈도우인 경우
        font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
        rc('font', family=font_name)
    else:    
    # Mac 인 경우
        rc('font', family='AppleGothic')
except : 
    pass
plt.rcParams['axes.unicode_minus'] = False  

data = pd.DataFrame({
    '이름': ['영식', '철수', '영희'],
    '나이': [22, 31, 25],
    '몸무게': [75.5, 80.2, 55.1]
})

st.dataframe(data, use_container_width=True)

fig, ax = plt.subplots()
ax.bar(data['이름'], data['나이'])
st.pyplot(fig)

barplot = sns.barplot(x='이름', y='나이', hue='이름', data=data, 
                      ax=ax, palette='Set2', legend=False)

fig = barplot.get_figure()
st.pyplot(fig)

#############
# matplotlib 의 gallery 에 많은 예제들 
# https://matplotlib.org/stable/gallery/index.html

species = (
    "Adelie\n $\\mu=$3700.66g",
    "Chinstrap\n $\\mu=$3733.09g",
    "Gentoo\n $\\mu=5076.02g$",
)
weight_counts = {
    "Below": np.array([70, 31, 58]),
    "Above": np.array([82, 37, 66]),
}
width = 0.5

fig, ax = plt.subplots()
bottom = np.zeros(3)

for boolean, weight_count in weight_counts.items():
    p = ax.bar(species, weight_count, width, label=boolean, bottom=bottom)
    bottom += weight_count

ax.set_title("Number of penguins with above average body mass")
ax.legend(loc="upper right")

st.pyplot(fig)

code = np.array([
    1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1,
    0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0,
    1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1,
    1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1])

pixel_per_bar = 4
dpi = 100

fig = plt.figure(figsize=(len(code) * pixel_per_bar / dpi, 2), dpi=dpi)
ax = fig.add_axes([0, 0, 1, 1])  # span the whole figure
ax.set_axis_off()
ax.imshow(code.reshape(1, -1), cmap='binary', aspect='auto',
          interpolation='nearest')

st.pyplot(fig)







