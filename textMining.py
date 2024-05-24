from konlpy.tag import *
import os
os.environ['JAVA_HOME'] = r'C:\Program Files\Java\jdk-17\bin'

# 형태소 분석기 객체 생성
okt = Komoran()

text = "안녕하세요, 김승원입니다. 형태소 분석기 자동화를 해보고 있습니다. 햄버거 맛있어요"

print("입력 텍스트 : ", text)
print("입력 텍스트 속 명사 리스트 : ", okt.nouns(text))

for noun in okt.nouns(text):
    if len(noun) >= 2:
        print(noun, end=" ")