# 숫자형이랑 숫자 형태로 이루어진 자료형(data type)
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


<<<<<<< HEAD
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
=======
print("pyhon's favorite food it perl")


say = "pyhon is very easy. he says"
print(say)
>>>>>>> a718f61caaa64928ba8b42490d9b99c6718e776c
