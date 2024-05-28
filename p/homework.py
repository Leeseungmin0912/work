#1. 사용자로부터 숫자를 입력받으면 양수인지 음수인지 판별하는 코드를 작성하라(단, 사용자가 X를 입력하면 프로그램이 멈춘다)

number = float(input("숫자를 입력하세요: "))

# 숫자가 0보다 큰지 여부 확인
if number > 0:
    print("입력한 숫자는 양수입니다.")
# 숫자가 0보다 작은지 여부 확인
elif number < 0:
    print("입력한 숫자는 음수입니다.")
# 숫자가 0인지 여부 확인
else:
    print("입력한 숫자는 0입니다.")



#2. 피보나치 수열이란 첫째와 둘째 항이 1이며 그 뒤의 모든 항은 바로 앞 두 항의 합인 수열을 말한다(ex: 1, 1, 2, 3, 5, 8, 13 …)  사용자가 생성 갯수를 입력하면 해당 갯수만큼 피보나치 수열을 생성하는 코드를 작성하라

#2번은 모르겠어요



#3. 아래 코드의 빈칸을 작성하여 딕셔너리의 키와 값을 올바르게 출력하라
# my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
#for _____ in _________:
   # print("키: ", key, ", 값: ", value)

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
for key, value in my_dict.items():
    print("키: ", key, ", 값: ", value)

#4.  '소수'란 1과 자기 자신 이외의 숫자로 나누어지지 않는 숫자를 말한다. 사용자로부터 숫자를 입력받으면 해당 숫자가 소수인지 아닌지를 판별하는 코드를 작성하라


def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    for i in range(3, number // 2 + 1, 2):
        if number % i == 0:
            return False
    return True

user_input = int(input("숫자를 입력하세요: "))
if is_prime(user_input):
    print(f"{user_input}은(는) 소수입니다.")
else:
    print(f"{user_input}은(는) 소수가 아닙니다.")


#5. 임의의 숫자를 생성한 후, 사용자가 숫자를 맞출때까지 반복실행하는 코드를 작성하라. (추가 조건: 만약 사용자가 답한 값이 임의의 값보다 작으면 up을 출력하고 임의의 값보다 높으면 down을 출력하라.)

import random

# 1부터 100 사이의 무작위 숫자 생성
target_number = random.randint(1, 100)

import random

def guessing_game():
    # 1부터 100 사이의 임의의 숫자를 생성합니다.
    random_number = random.randint(1, 100)
    
    while True:
        user_input = int(input("숫자를 입력하세요 (1에서 100 사이): "))
        
        if user_input < random_number:
            print("Up")
        elif user_input > random_number:
            print("Down")
        else:
            print(f"축하합니다! 숫자 {random_number}을(를) 맞췄습니다.")
            break