# 91~100점 A+ 
# 81~90 B+
# 71~80 C+
#나머지는 F이다
#출력은 xxx학생의 학점은 ##이다

'''print('점수를 입력해주세요')
score = int(input())

if score >= 91:
    print('xxx학생의 학점은 A+입니다')
if score >= 81:
    print('xxx학생의 학점은 B+입니다.')
if score >= 71:
    print('xxx학생의 학점은 C+입니다.')
else:
    print('xxx학생의 학점은 F입니다.')



name = '이승민'
score = 101

if score > 100:
    pass

elif score >= 91:
    grade = 'A+'
elif score >= 81:
    grade = 'B+'
elif score >= 71:
    grade = 'C+'
else:
    grade = 'F'


if score > 100:
    print('잘못된 점수 입니다.')
else:
    print(f'{name}학생의 학점은 {grade}이다')

#while 문

# 가장 간단한 while문 예시



#input 활용 while문

prompt = """
1. ADD
2. DEL
3. LIST
4. QUIT

Enter number: """
number = 0
while number != 4:
    print(prompt)
    number = int(input())
'''
#break ( while 강제 종료)
coffee = 10
money = 300
while money:
    print('돈을 받았으니까 커피를 줍니다')
    coffee -= 1
    print('남은 커피의 양은 {coffee}개 입니다.' % coffee)
    if not coffee:
        print('커피가 다 떨어졌습니다')
        break