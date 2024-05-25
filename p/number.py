#조건에 맞지 않는 경우 맨 처음으로 돌아기기
# 1~10까지 정수 중 홀수만 출력하기

#첫번째 문제
# while 문을 사용하여 1~10까지 차례대로 출력하세요

a = 0

while a < 10:
    a += 1
    print(a)

#두번째 문제
#while문을 사용하여 사용자에게 숫자를 입력받고
#해당 숫자 ~ 0 까지 거꾸로 (카운트다운) 출력하세요
# 예시: 사용자가 7을 입력할 경우 - 7 6 5 4 3 2 1 0 순서로
print('숫자를 입력하세요')
i = int(input())
while True:
    if i == -1:
        break
    print(i)
    i -= 1

#세번째 문제
#사용자가 특정 수를 입력하면 해당 수의 팩토리얼을 출력하는 while문을 입력하세요
n = int(input('숫자를 입력하세요'))
fact_num = 1
while n >= 0:
    fact_num = fact_num * n
    n = n - 1
print('|n{0}! = {1}입니다',format(input(input_number,fact_num)))
    

#네번째 문제
# 사용자가 quit라고 입력하면 while문을 종료하고
# 아닐경우사용자가 입력한 값을 출력하세요(quit이 들어올때까지 while 실행)
while True:
    user_input = input('입력하세요(종료하려면 quit 입력):')
    if user_input == 'quit':
        print('프로그램 종료')
        break

#마지막 문제
#사용자로부터 숫자를 입력받고
#해당 수 만큼 임의의 숫자를 입력받은 뒤
#입력받은 수를 거꾸로 출력하세요


n = int(input('몇 개?'))
numbers = []

#입력단
i = n - 1
while i >= 0:
   print(numbers[i])
   i -= 1