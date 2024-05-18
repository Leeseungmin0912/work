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


print("pyhon's favorite food it perl")


say = "pyhon is very easy. he says"
print(say)