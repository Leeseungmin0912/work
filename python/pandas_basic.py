#외부 라이브러리 임포트

import pandas as pd

# 딕셔너리 생성
dict_data = {'a':1, 'b':2, 'c':3}

#pands 시리즈 함수로 딕셔너리를 시리즈로 변환하여 sr에 저장
sr = pd.Series(dict_data)
print(sr)

#시리즈 인덱스 목록
sr.index

#시리즈의 값 목록
sr.values

#리스트를 시리즈로 변환
list_data = ['2019-0102',3.14,'ABC',100,True]
sr = pd.Series(list_data)
print(sr)

sr.index    

sr.values

#튜플을 시리즈로 변환
tup_data = ('영인','2010-05-01','여성',True)
sr = pd.Series(tup_data, index=['이름','생년월일','성별','학생여부'])
print(sr)

#셀렉
print(sr[0])
print(sr['이름']) #딕셔너리에서 키로 접근하는 것은 동일하다(단, 시리즈에서만)

#다중셀렉
print(sr[[1,2]])
print(sr[['생년월일','성별']])

#다중셀렉 슬라이싱
print(sr)
print(sr[1:3])
print(sr['생년월일','성별'])

#딕셔너리 생성
dict_data = {'c0':[1,2,3],'c1':[4,5,6],'c2':[7,8,9],'c3':[10,11,12],'c4':[13,14,15]}

# 딕셔너리를 데이터 프레임으로 변환
df = pd.DataFrame(dict_data)


# 리스트를 데이터프레임으로 바로 변환
df = pd.DataFrame([[15,'남자','덕영중'],[17,'여자','선린중']]),
index=['준서','예은']
columns = ['나이','학교','성별']

#df의 인덱스 리스트
df.index

#행 인덱스, 컬럼 이름 변경하기

df.index = ['학생1','학생2']


#df의 컬럼 리스트
df.columns


#대응하여 변환하기

df.rename(columns={'나이':'연령','성별':'남녀','학교':'소속'}, inplace=True)


#데이터프레임 복제
df2 = df
df2

#인덱스 삭제 
df2.drop('우현')


#데이터프레임 컬럼 삭제

df4 = df.copy()
df4.drop('수학',axis =1, inplace = True)

#다중 컬럼 삭제(영어 음악)
df5 = df.copy()

df5 = drop(['영어, 음악'], axis =1, inplace = True)
df5


#LOC , iLOC = 로우셀렉
df['영어']
label1 = df.loc['서준']
position1 = df.iloc[0]
print('')
print(position1)


# 로우 인덱스를 사용하여 2개 이상의 인덱스 선택
label2 = df.loc[0['서준','우현']]
position2 = df.iloc[[0,1]]
print(label2)
print('')
print(position2)





#인덱서 슬라이싱
label3 = df.loc['서준':'우현']
position3 = df.iloc[0,2]
print(label3)
print('')
print(position3)

#불린 인덱서

mask = df.index == '서준'



#컬럼 셀렉
math1 = df['수학']
print(type(math1))


# 컬럼셀렉 다른 방법
eng  = df.영어
print(eng)


# 다중컬럼 : 음악, 체육 점수
music_gym = df[['음악','체육']]
music-gym


#인덱스 재설정

df.set_index('이름',inplace= True)


#데이터프레임 df의 특정 원소 1개를 선택(서준이의 음악점수)

a = df.loc['서준','음악']
print(a)


a = df.iloc[0, 2]
print(a)

a = df.loc['서준',['음악','체육']]
peint(a)

b = df.iloc[0,[4]]
print(b)

#서준이와 우현이의 음악과 체육 점수

g = df.loc[['서준','우현'],['체육','음악']]
print(g)

h = df.iloc[[0,1],[2,3]]
print(h)

i = df.loc['서준':'우현','음악':'체육']
print(i)

#add columes
#데이터프레임에 국어 컬럼을 추가




































































# 두 학생의 과목별 사칙연산 수행

add = student1 + student2
sub = student1 - student2
mul = student1 * student2
div = student1 / student2



# 4개의 시리즈를 합쳐서 하나의 데이터프레임으로 만들기

df = pd.DataFrame([add, sub, mul, div], index = ['덧셈','뺄셈','곱셈','나눗셈'])
df

#라이브러리 임포트

import numpy as np

student1 = pd.Series({'국어':np.nan, '영어':80,'수학':90})
student2 = pd.Series({'수학':80, '국어':70})

#데이터에 null값이 있을 때 사칙 연산
add = student1.add(student2, fill_value=0)
sub = student1.sub(student2, fill_value=0)
mul = student1.mul(student2, fill_value=0)
div = student1.div(student2, fill_value=0)

df = pd.DataFrame()

import seaborn as sns
titanic  = sns.load_datatest('titanic')
titanic

#titanic 데이터셋에서 age, fare 2개 열을 선택하여 데이터프레임 새로 만들기

df = titanic.loc[:,['age','fare']]
df.head(10)


#데이터 프레임 투 넘버

add = df + 10



#데이터 프레임끼리 계산

sub = add - df
sub.head()







a = df['Name','Age','Country','MARRIED',['CINA','JENNY','BELA','ALEX','LIAM','SAM'],[29, 26, 26, 35, 32, 30],['VIETNAM','TAIWAN','USA','SOUTH KOREA','ENGLAND','TAIPEI'],[0,0,0,0,0,1]]