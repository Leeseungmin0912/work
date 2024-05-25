#2024/05/18


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

#TUPLE
#튜플은 리스트와 매우 흡사한 자료형태
#그러나 튜플은 문자열과 마찬가지로 불변성을 가짐

#튜플선언
t1 = () #빈튜플
t2 = (1,2,3) #정수로 구성된 튜플
t3 = (1,) #원소값 하나만 생성
t4 = 1,2,3 #괄호를 생략하면 튜플로 생성됨
t5 = (1,2,(3,4)) #이중 튜플 생성

#타입 확인
type(t5)

#튜플의 불변성
t1 = (1,2,3,4) #튜플 안에 들어있는 값은 삭제나 추가가 되지 않음

#튜플의 인덱싱과 슬라이싱
#인덱싱
t1 = (1,2,3,4)
print(t1[0])
print(t1[1:])

#튜플 더하기
t1 = (1,2,3,4,5)
t2 = (5,6)
print(t1+t2)

#딕셔너리  
#딕셔너리는 키값에 대응하는 벨류값을 구성하여 쌍으로 묶은 데이터 형태
# ㄱ = [가방, 나비], ㄴ = [나비, 노래]등을 대응관계를 가지고 있음
#이렇게 데이터끼리 대응관계를 가지는 형태를 "해시(hash)"라고 부름(json,dataframe등)

#딕셔너리 생성
dic = {'name':'pey','phone':'010-7564-2629','birth':'0912'}
type(dic)


#key는 고유성만 가지면, 정수와 문자열을 모두 사용할 수 있습니다.
a = {1:'hi', 1:'hello'}
print(a[1])

#하나의 key에 여러개의 원소 밸류 생성
a = {'a':[1,2,3]}

#딕셔너리에 쌍 추가하기
a = {1:'a'}
a['new'] = 2 #매우 중요
print(a)

#딕셔너리의 원소 삭제
del a[1]
print(a)

#딕셔너리의 접근(데이터 출력)
grade = {'pey':10, 'julliet':99}
print(grade['pey'])

#주의사항 key는 반드시 불변성을 가져야한다.
#a = {[1,2]:'hi'}
#a = {(1,2):'hi'}
#print(a[1,2])


#키와 다르게 밸류는 중복이든, 리스트든 상관없이 만들 수 있다.
a = {'클래스':['최재욱','최종대','김종한','김종한']}
print(a['클래스'])


#2024/05/25

#딕셔너리의 내장함수
#딕셔너리 선언

a = {'name':'pey','phone':'010-7564-2629','birth':'0912'}
#내가 선언한 딕셔너리에서 키값만 모아서 반환받기


print(a.keys())

#바로 리스트로 만들려면? 만들고싶은 자료형(객체)
b = list(a.keys())
print(b)


#value 값을 모아서 리스트로 반환받기
print(a.values())

#key , value에 쌍 얻기
print(a.items())

#key , vlaue에 모든 쌍 지우기

#print(a.clear())

#key로 value 얻기
print(a['phone'])
print(a.get('phone'))

#print(a['gender'])  <- keyError
print(a.get('gender')) # None을 출력

#key 값이 없으면, 사용자가 디폴트 갓을 지정해서 가져오기
print(a.get('gender','female'))




# Set 자료형
#세트 만들기
s1 =  set([1,2,3])
print(s1)
print(type(s1))

#세트는 중복을 허용하지 않는다
#세트는 순서가 없다.(이터레이블자료형이 아니다.)
s2 = set('hello')
print(s2)


# 세트 교집합 구하기 -&(and 이면서)
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
#이때 교집합 수는 4,5,6
print(s1 & s2)
print(s1.intersection(s2))
print(s1 and s2) #논리 연산자 이기 때문에 마지막에 있는 것을 반환함


# 합집합 - | (or 이거나)
print(s1 | s2)
print(s1.union(s2))
print(s1 or s2)


#차집합 ('-')
print(s1 - s2)
print(s2 - s1)

#BOOL (BOOLEAN)
#불 또는 불린 자료형이란 참과 거짓(Ture & False)를 나타내는 자료형
#불 자료형은 두가지 값만 가지고 있다.

#불선언
true = 1 #Syntax Error

#올바른 불 자료형 만들기
a = True
b = False
type(a),type(b)

#불 자료형은 보통(거의대부분) 조건문의 리턴값으로 사용
print(1 == 1)
print(1 > 2)
print(3 >= 3)


#자료형의 참과 거짓
# 이진법의 불린
print(0 == True)
print(1 == True)

#자료형의 불린
#자료에 원소값이 있으면 True를 원소값이 없으면 False를 리턴한다
print(bool([1,2,3]))
print(bool([]))
print(bool({}))
print(bool({1,2,3}))


#  @제어문

# 조건(if)문

#돈이 있으면 택시타고 없으면 걸어가라

money = 1
if money:
    print('택시하세요')
else:
    print('걸어가세요')



#만약 3000원 이사으이 돈을 가지고 있으면 택시를 타고 그렇지 않으면 걸어가라

print('가지고 있는 돈을 입력하세요 >>>',end='')
money = int(input())

if money >= 3000:
    print('택시를 타세요')

else:
    print('걸어가세요')



#돈이 3000원 이상 있거나 풀러줄 시계가 있다면 택시를 타고 아니면 걸어가라

print('돈을 입력하세요')
money = int(input())

print('시계가 있나요?')

yes = 1
no = 2
watch = int(input())

if money >= 3000 or watch:
    print('택시타세요')

else:
    print('걸어가세요')


#not = 특정 원소가 해당 자료형에 있는가?
# 만약 주머니에 돈이 있으면 택시를 타고, 없으면 걸어가라
poket = ['paper','phone','money']
if 'money' in pocket:
    print('택시타라')
else:
    print('걸어가라')

#지갑에 돈이 있으면 택시를 타고, 지갑에 돈이 없지만 시계가 있으면 택시를 타고, 돈도 없고 시계도 없으면 걸어가라

pocket = ['papper','phone']
watch = 1
if 'money'in pocket:
    print('택시타라')
else:
    if watch:
        print('택시타라')
    else:
        print('걸어가라')

#elseif의 편리함
pocket = ['papper','phone']
watch = 1
if 'money'in pocket:
    print('택시타라')

elif watch:
    print('택시타라')

else:
    print('걸어가라')


# pass의 편리함
pocket = ['papper','phone','money']
if 'money' in pocket:
    pass
else:
    print('걸어가라')

