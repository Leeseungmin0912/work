#초기 커피 갯수는 10개 입니다.
#커피가격은 300원입니다.
#사용자에게 돈을 입력받습니다.
#사용자가 300원을 정확히 입력하면 커피를 주고 남은 커피의 갯수를 출력합니다.
#사용자가 300원보다 많은 돈을 입력하면 차액을 거스름돈으로 주고, 남은 커피 갯수를 출력합니다.
#사용자가 300원보다 적은 돈을 입력하면 돈을 다시 주고, 남은 커피 갯수를 출력합니다.
#커피가 다 떨어지면 판매를 중지한다는 메시지와 함께 자판기 코드를 뺍니다


coffee = 10

while True:
    money = int(input('돈을 입력해주세요'))

    if money == 300:
        print('커피를 줍니다')
        coffee -= 1
        print(f'커피가 {coffee}개 남았습니다')

    if not coffee:
        print('커피가 다 떨어졌습니다')
        break

    elif money > 300:
        print('거스름 돈과 커피를 줍니다')
        coffee -= 1
        print(f'커피가 {coffee}개 남았습니다')
        print(money - 300,'원을 반환합니다.')

    if not coffee:
        print('커피가 다 떨어졌습니다')
        break

    elif money < 300:
        print('돈을 다시 돌려줍니다.')
        print(f'커피가 {coffee}개 남았습니다')

        if not coffee:
            print('커피가 다 떨어졌습니다')
            break