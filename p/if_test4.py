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
            print(Teenager_money * 1,"원입니다")
        elif companion == 2:
            print(Teenager_money * 2,"원입니다")
        elif companion == 3:
            print(Teenager_money * 3,"원입니다")
        elif companion == 4:
            print(Teenager_money * 4,"원입니다")
        elif companion == 5:
            print(Teenager_money * 5,"원입니다")
    else:
        print(f'당신은 어린이 입니다. 결제 금액은 {kid_money}원 입니다')

        print('같이 온 동행자가 몇명인가요 (최대 5인까지 가능합니다.)')

        companion = int(input())
        if companion == 1:
            print(kid_money * 1,"원입니다")
        elif companion == 2:
            print(kid_money * 2,"원입니다")
        elif companion == 3:
            print(kid_money * 3,"원입니다")
        elif companion == 4:
            print(kid_money * 4,"원입니다")
        elif companion == 5:
            print(kid_money * 5,"원입니다")
        
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
            print(night_Adult_moneyAdult_money * 1,"원입니다")
        elif companion == 2:
            print(night_Adult_money * 2,"원입니다")
        elif companion == 3:
            print(night_Adult_money * 3,"원입니다")
        elif companion == 4:
            print(night_Adult_money * 4,"원입니다")
        elif companion == 5:
            print(night_Adult_money * 5,"원입니다")
    elif age == 2:
        print(f'당신은 청소년 입니다. 결제 금액은 {night_Teenager_money}원 입니다.')

        print('같이 온 동행자가 몇명인가요 (최대 5인까지 가능합니다.)')

        companion = int(input())
        if companion == 1:
            print(night_Teenager_money * 1,"원입니다")
        elif companion == 2:
            print(night_Teenager_money * 2,"원입니다")
        elif companion == 3:
            print(night_Teenager_money * 3,"원입니다")
        elif companion == 4:
            print(night_Teenager_money * 4,"원입니다")
        elif companion == 5:
            print(night_Teenager_money * 5,"원입니다")
    else:
        print(f'당신은 어린이 입니다. 결제 금액은 {night_kid_money}원 입니다.')

        print('같이 온 동행자가 몇명인가요 (최대 5인까지 가능합니다.)')

        companion = int(input())
        if companion == 1:
            print(night_kid_money * 1,"원입니다")
        elif companion == 2:
            print(night_kid_money * 2,"원입니다")
        elif companion == 3:
            print(night_kid_money * 3,"원입니다")
        elif companion == 4:
            print(night_kid_money * 4,"원입니다")
        elif companion == 5:
            print(night_kid_money * 5,"원입니다")


print('식사 쿠폰도 구매하시겠습니까? 한식은"1만원", 일식은"15000원", 중식은"2만원"입니다.')

yes = 1
no = 2

korean_food = 1
japanese_food = 2
chinese_food = 3

meal_buy = int(input('식사 쿠폰을 구매하시고 싶으시면 "1번" 구매를 하지 않으실거라면 "2번"을 눌러주세요'))

if meal_buy == 1:
    print('식사 쿠폰 구매를 입력해주셨습니다. 어느 식사를 드시겠습니까?')
    meal = int(input('한식은 "1번" 일식은 "2번" 중식은 "3번"입니다.'))

    if meal == 1:
        print('한식을 선택하셨습니다. 결제 금액은 10000원 입니다.')
        a = 10000
    if meal == 2:
        print('일식을 선택하셨습니다. 결제 금액은 20000원 입니다.')
        b = 20000
    if meal == 3:
        print('중식을 선택하셨습니다. 결제 금액은 30000원 입니다.')
        c = 300000

print('결제는 무엇으로 하시겠습니까? 카드는"1번", 현금은 "2번을"눌러주시고 앞쪽 데스크로 이동해주세요.')

card_buy = 1
cash_buy = 2

payment = int(input())

if payment == 1:
    print('카드를 카드 리더기에 꼽아주세요')

if payment == 2:
    print('앞쪽 데스크로 이동해주세요')

print('이용해주셔서 감사합니다. 즐거운 시간 보내세요')