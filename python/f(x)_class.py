def sum(a,b):
    result = a + b
    return result

# 매개 변수가 없는 함수의 예

def say():
    return 'Hi'

print(say())

# 리턴이 없는 함수의 예

def sum(a,b):
    '''print로 출력하고 return 하지 않는 함수'''
    print(f'{a},{b}의 합은 {a+b}입니다.')


#조건에 따라 동작하는 sum_mul 함수
def sum_mul(choice, *args):
    '''첫번쨰 파라미터가 sum이면, 그 뒤에 정수들을 더하고,
    첫번째 파라미터가 mul이면 그 뒤에 정수들을 곱하는 함수'''

    if choice == 'sum':
        result = 0
        for i in args:
            result = result + i
    elif choice == 'mul':
            result = 1
            for i in args:
                result = result* i
    return result




#연습문제

#1. 빼기 연산을 하는 함수를 만들고 호출하세요
#파라미터 두개를 입력바당 해당 파리미터가 문자열이면 '정수를 입력하세요'를 출력하고 정수형이면 곱하는 함수를 만들고 호출하세요


def string_or_int(a,b):
    print()
