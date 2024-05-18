# 숫자형이랑 숫자 형태로 이루어진 자료형(data tye)
# 123과 같은 정수, 12.3과 같은 실수 또는 8진수와 16진수 등이 있다.
# 정수형
a = 123
a = -123
a =1
print(a)



# 실수형 데이터
a = 1.2
a = -3.45
print(a)


# 실수형 데이터의 지수표현방식
a = 4.23e10
print(a)

# 8진수는(octal)
# 8진수는 숫자가 0o 또는 0O로 시작한다
a = 0o177
print(a)



# 16진수(Hexadecimal)
# 16진수는 0x로 시작

a = 0xABC
print(a)


# 숫자형의 연산자
a = 3
b = 4
print(a+b)  # 더하기
print(a-b)  #빼기
print(a*b)  #곱하기
print(a/b)  #나누기


# x의 y제곱 연산자
a = 3
b = 4
print(a**b)


#나눗셈 후의 나머지를 리턴하는 연산자
#나눗셈 후의 몫을 리턴하는 연산자
a = 7
b = 3
print(a%b)  #나머지 연산자
print(a//b) #몫 연산자


#문자열
# 문자열(String , object)이란 문자와 단어로 구성된 집합 자료형
# 큰 따옴표 또는 작은 따옴표로 감싸면 해당 데이터는 문자열이 됨
# 숫자형이든 다른 집합자료형이든 따옴표로 감싸면 문자열로 변경됨
print("I love python")
print(123)

#작은 따옴표도 똑같이 적용된다.
print('123')


#따옴표 3개 연속으로 사용할 수 있다.
print("""I love python""")
print('''I love python''')



print("python's favorite food it perl")


say = "'python is very easy'. he says"
print(say)

# 이스케이프 코드
food = 'python\'s favorite food is perl'
say = "\"python is very easy.\" he says"
print(food,say)


# 여러줄인 문자열을 변수에 대입할 때
# 이스케이프코드
multiline = 'Life is too short\n You need python'
print(multiline)

#따옴표 3개 줄바꿈
multiline = '''Life is too short
You need python'''
print(multiline)

#문자열의 연산
# 파이썬에서는 문자열을 더하거나 곱할 수 있다.
#문자열 더하기
head = 'python'
tail = ' is fun'
print(head + tail)

#문자열 곱하기
a = '안녕하세요'
print(a*3)

# ================
# My Program
# ================
#을 출력하세요
a = '='
b = 'My Program'
c = '='
print(a*10)
print(b)
print(c*10)

#이터레이블
# 문자열은 위치속성을 가지고있는 이터레이블 데이터 타입이다.
# 문자열의 길이 구하기
a = 'Life is too short'
print(len(a))

# 문자열의 인덱싱
a = 'Life is too short, You need python'
print(a[3])
print(a[33])
print(a[-1])


#슬라이싱
# 문자열에서 특정 단어를 출력
a = 'Life is too short, You need python'
print(a[0] + a[1] + a[2] + a[3])

#슬라이싱은 이터레이블[시작번호:끝번호]
#단, 끝번호에 해당하는 원소는 버림
print(a[0:4])


#슬라이싱 할 때 항상 시작번호가 0일 필요는 없다.
print(a[:3])  #Lif
print(a[:4])  #Life

#슬라이싱 할 때 항상 끝번호가 마지막 위치번호일 필요는 없다.
print(a[28:34]) #python
print(a[28:])  #python

#예제
print(a[:]) #슬라이싱 코드를 이렇게 짜면 어떻게 될것인가
# 처음부터 끝까지 다 가져온다.



#아래 주어진 문자열에서 월일(0000) = date라는 변수에 저장하세요
#날씨 = weather라는 변수에 저장하세요
#print문을 사용하여 날짜와 날씨를 출력하세요

data = '20240518 sunny'
date = (data[4:8]) #날짜
weather = (data[9:]) #날씨
print(date, weather) #결과값


#불변성(immutable)
a = 'pithon'
a = a[:1] + 'y' + a[2:]
print(a)


#문자열 포매팅
#숫자대입 = 포맷코드 %d
print('I eat %d apples.' %3)

#문자대입 = 포맷코드 %5
print('I eat %s apples'% 10)

#어차피 파이썬에서 따옴표 안의 원소는 문자열로 포맷되기때문에 %s로 통일할 수 있다.
number = 10
day = 'three'
print('I ate %s apples. so I was sicj %s days' %(number, day))

a = '='
print(a*100,'\nMy program\n' + a*100)

#소켓 포매팅
print('I eat {0} apples'.format(3))

print('I eat {0} apples. So I was sick for {1} days '.format(number,day))

#이름으로 접근
print('I ate {number} apples. So I was sick for {day} days'.format(number=10, day='three'))

print('I ate {0} apples. So I was sick for {day} days'.format(10, day='three'))


# f-string 강사추천

name = '이승민'
age = 17
print(f'나의 이름은 {name}이며, 나이는 {age}입니다.')

# f-string 소켓 연산
print(f'저는 내년이면 {age+1}살이 됩니다.')

# f-string 문자열 정렬
print(f"{'hi':<10}")
print(f"{'hi':>10}")
print(f"{'hi':^10}")

print('='*50)
print(f"{'My Program':^50}")
print('='*50+ '\n' + f"{'My Program':^50}" + '\n' + '='*50)


#공백에 원소 채워넣기 f - string
print(f'{"hi":=^10}')
print(f'{"hi":!<10}')

#소수점 표현 f- string
y = 3.141592
print(f'{y:.4f}')

#문자열 관련 내장함수

#문자열에 포함된 원소에 개수 세기
a = 'hobby'
print(a.count('b'))

#인덱스의 위치를 알려주는 함수
a = 'python is the best choice'
print(a.find('i'))

#인덱스 위치 조회2
print(a.index('i'))


#문자열 삽입
a = 'abcd'
print(','.join(a))


#'hi','HI' -> 유니코드
# 소문자를 대문자로 바꾸어주는 함수
a ='hi'
print(a.upper())

a = 'HI'
print(a.lower())


#왼쪽 공백 지우기
a  = ' hi '
print(a.lstrip()) #왼쪽공백 지우기
print(a.rstrip()) #오른쪽공백 지우기
print(a.strip()) #양쪽 공백 지우기

# 문자열 바꾸기
a = 'Life is too short'
print(a.replace('Life','Your leg')) #Life 를 Your leg로 바꾸는 함수

#문자열 나누기
a = 'Life is too short'
print(a.split())

b = 'a:b:c:d'
print(b.split(':'))


#리스트
#숫자와 문자열 데이터타입 등 구성된 원소를 집합의 개념으로 묶어놓은 자료형
#앞으로 배울 자료형 중 가장 많이 사용 됨

#리스트 선언
a = [1,3,5,7,9]
print(a)

#타입확인
print(type(a))


#리스트를 선언할때 다양한 원소를 담을 수 있음
a = [] #빈리스트
b = [1,2,3] #정수만 담긴리스트
c = ['life', 'is', 'too', 'show'] #문자열만 담긴 리스트
d = [1,2,['life','is']] #정수와 문자열을 혼용해서 담은 리스트
e = [1,2,['life','is']] #리스트 안에 리스트도 담을 수 있음

#리스트는 파이썬의 대표적인 이터레이블 자료형(iterrable = 순회가능한)

a = [1,2,3]
print(len(a))

# 0번 원소에 접근
print(a[0])

#문자열과 다른점
#리스트는 원소끼리의 연산이 가능함
print(a[0] + a[2])

#리스트안에 또 다른 리스트가 있을 때 인덱싱하는 방법
a = [1,2,3,['a','b','c']]
print(len(a))

#'a'추출하기
print(a[3][0])


#다음 리스트에서 'Life'를 출력하세요
a = [1,2,['a','b',['Life','is']]]
print(a[2][2][0])


#리스트슬라이싱

A = [1,2,3,4,5]
print(a[:3])

#중첩 슬라이싱
a = [1,2,3,['a','b','c'],4,5]
print(a[3][:2])


#리스트 연산하기
# 리스트의 덧셈

a = [1,2,3]
b = [4,5,6]
print(a+b)

# 리스트의 곱셈
print(a*3)

# 리스트 원소값 수정
a = [1,2,3]
a[1] = 4
print(a)

#리스트 원소값 삭제
#단일원소 삭제 
a = [1,2,3]
del a[1]
print(a)


#다중원소 삭제
a = [1,2,3,4,5]
del a[2:]
print(a)


#리스트에 원소값을 추가해주는 함수
a = [1,2,3]
a.append(4)
print(a)

#리스트의 정렬
a = [1,4,3,2]
a.sort()
print(a)

#리스트의 정렬
a = [1,2,3,4]
a.sort(reverse=False)
print(a)

#리스트 원소 뒤집기
a = ['a','b','c']
a.reverse()
print(a)

#리스트 인덱스 반환
print(a.index('b'))

#리스트 요소 삽입
#리스트 a번째 위치에 b를 삽입하는 함수
a = [1,2,3]
a.insert(0,61)


#리스트 원소 제거
a = [1,2,3,1,2,3]
a.remove(3)
print(a)

#pop - 리스트의 요소를 끄집어내기
a = [1,2,3]
b = a.pop(0)
print(a)
print(b)

#리스트에 포함된 원소 x의 갯수 세기
a = [1,2,3,1]
a.count(1)

#extend - 리스트 확장
a = [1,2,3]
a.extend([4,5])
print(a)