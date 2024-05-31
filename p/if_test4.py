'''
x = int(input('숫자를 입력해주세요 >>>'))


#17 

if x > 10:     # x가 10 이상인 수 인가를 물어보는 코드
    if x % 2 == 0: # x를 2로 나누면 딱 떨어지는지 물어보는 함수
        print('10초과 짝수') # 딱 떨어진다면 10을 초과하는 짝수를 출력함

    else: # 만약 그렇지 않는다면 작동하는 코드
        print('10초과 홀수') # 10초과 홀수를 출력하는 코드

else: # 6번 줄 if가 작동하지 않으면 작동하는 코드
    print('10이하') # 10이하를 출력하는 코드
'''




#놀이동산 요금 계산

Adult_money = 15000
Teenager_money = 10000
kid_money = 50000

night_Adult_money = 10000
night_Teenager_money = 5000
night_kid_money =  3000

night = 1
afternoon = 2

time = int(input('야간은 "1번" 주간은 "2"번을 입력해주세요 >>>'))

if time == 1:

    Adult = 1
    Teenager = 2
    kid = 3
    age = int(input('당신이 성인이면"1번", 당신이 청소년이면"2번" 당신이 어린이면 "3번"을 눌러주세요 >>>'))

    if age == 1:
        print(f'당신은 성인입니다 1인 결제 금액은 {Adult_money}원 입니다')

        print('같이 온 동행자가 몇명인가요 (최대 5인까지 가능합니다.)')

        companion = int(input())
        if companion == 1:
            print(Adult_money * 1,"원입니다")
        elif companion == 2:
            print(Adult_money * 2,"원입니다")
        elif companion == 3:
            print(Adult_money * 3,"원입니다")
        elif companion == 4:
            print(Adult_money * 4,"원입니다")
        elif companion == 5:
            print(Adult_money * 5,"원입니다")

    elif age == 2:
        print(f'당신은 청소년 입니다 결제 금액은 {Teenager_money}원 입니다')

        print('같이 온 동행자가 몇명인가요 (최대 5인까지 가능합니다.)')

        companion = int(input())
        if companion == 1:
            print(Adult_money * 1,"원입니다")
        elif companion == 2:
            print(Adult_money * 2,"원입니다")
        elif companion == 3:
            print(Adult_money * 3,"원입니다")
        elif companion == 4:
            print(Adult_money * 4,"원입니다")
        elif companion == 5:
            print(Adult_money * 5,"원입니다")
    else:
        print(f'당신은 어린이 입니다. 결제 금액은 {kid_money}원 입니다')

        print('같이 온 동행자가 몇명인가요 (최대 5인까지 가능합니다.)')

        companion = int(input())
        if companion == 1:
            print(Adult_money * 1,"원입니다")
        elif companion == 2:
            print(Adult_money * 2,"원입니다")
        elif companion == 3:
            print(Adult_money * 3,"원입니다")
        elif companion == 4:
            print(Adult_money * 4,"원입니다")
        elif companion == 5:
            print(Adult_money * 5,"원입니다")
        
    print('같이 온 손님이 몇명인가요?')

    

if time == 2:
    
    Adult = 1
    Teenager = 2
    kid = 3
    age = int(input('당신이 성인이면"1번", 당신이 청소년이면"2번" 당신이 어린이면 "3번"을 눌러주세요 >>>'))

    if age == 1:
        print(f'당신은 성입니다 결제 금액은{night_Adult_money}원 입니다.')

        print('같이 온 동행자가 몇명인가요 (최대 5인까지 가능합니다.)')

        companion = int(input())
        if companion == 1:
            print(Adult_money * 1,"원입니다")
        elif companion == 2:
            print(Adult_money * 2,"원입니다")
        elif companion == 3:
            print(Adult_money * 3,"원입니다")
        elif companion == 4:
            print(Adult_money * 4,"원입니다")
        elif companion == 5:
            print(Adult_money * 5,"원입니다")
    elif age == 2:
        print(f'당신은 청소년 입니다. 결제 금액은 {night_Teenager_money}원 입니다.')

        print('같이 온 동행자가 몇명인가요 (최대 5인까지 가능합니다.)')

        companion = int(input())
        if companion == 1:
            print(Adult_money * 1,"원입니다")
        elif companion == 2:
            print(Adult_money * 2,"원입니다")
        elif companion == 3:
            print(Adult_money * 3,"원입니다")
        elif companion == 4:
            print(Adult_money * 4,"원입니다")
        elif companion == 5:
            print(Adult_money * 5,"원입니다")
    else:
        print(f'당신은 어린이 입니다. 결제 금액은 {night_kid_money}원 입니다.')

        print('같이 온 동행자가 몇명인가요 (최대 5인까지 가능합니다.)')

        companion = int(input())
        if companion == 1:
            print(Adult_money * 1,"원입니다")
        elif companion == 2:
            print(Adult_money * 2,"원입니다")
        elif companion == 3:
            print(Adult_money * 3,"원입니다")
        elif companion == 4:
            print(Adult_money * 4,"원입니다")
        elif companion == 5:
            print(Adult_money * 5,"원입니다")

print('이용해주셔서 감사합니다. 즐거운 시간 보내세요')