from konlpy.tag import *
import os
# 정규 표현식을 위한
import re
import pandas as pd

# 막대 그래프
import seaborn as sns

# 막대 그래프에 형태소 추가
import matplotlib.pyplot as plt

os.environ['JAVA_HOME'] = r'C:\Program Files\Java\jdk-17\bin'

# 형태소 분석기 객체 생성
okt = Komoran()
speech = open('speech.txt', encoding='UTF-8').read()
korSpeech = re.sub('[^가-힣]', ' ', speech)
print(korSpeech)

nonse = okt.nouns(korSpeech)

df_speech = pd.DataFrame({'speech': nonse})  # 글자 수를 의미하는 열을 추가한다.
df_speech['count'] = df_speech['speech'].str.len()  # 글자 수를 의미하는 열을 추가한다.
df_speech = df_speech.query('count >= 2')   # 2글자 이상만 꺼내서 저장
df_speech = df_speech.sort_values('count')  # 글자수 순서대로 정렬
print(df_speech)

# 단어를 기준으로 그룹화, 갯수를 다 합친 뒤 내림차순으로 출력
df_speech = df_speech.groupby('speech', as_index=False).agg(n=('speech', 'count')).sort_values('n',ascending=False)
top20 = df_speech.head(20)

# font.family = 폰트 설정 , figure.dpi = 해상도 설정 , figure.figsize =  가로세로 크기 조정
plt.rcParams.update({'font.family': 'Malgun Gothic', 'figure.dpi': '150', 'figure.figsize': [7, 6]})
sns.barplot(data=top20, x='n', y='speech')
plt.show()
