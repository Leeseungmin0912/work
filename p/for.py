#for 문
test_list = ['one','two','three']

for i in test_list:
    print(i)


#다양한 for 문의 활용

a = [(1,2),(3,4),(5,6)]
for first, last in a:
    print(first + last)

#for 문의 응용
score = [90, 25, 67, 45, 80]
number = 0

for mark in score:
    number += 1
    if mark >= 60:
        print(f'{number}번 학생은 불합격 입니다.')

#enumerate함수
score = [90, 25, 67, 45, 80]
for i, mark in enumerate(score):
    if mark >= 60:
        print(f'{i+1}번 학생은 합격입니다.')
    else:
        print(f'{i+1}번 학생은 불합격입니다.')

#합격한 학생들만 출력문 출력하기
# for문이 countinue

score = [90, 25, 67, 45, 80]

for i, mark in enumerate(score):
    if mark < 60:
        countinue
    print(f'{i+1}번 학생은 합격입니다')

    #range 함수

a = range(10)
print(a)

# 1~ 10까지 값을 더해보자

sum = 0

for i in range(1, 11):
    sum = sum + i
print(sum)

# 구구단 for문
for i in range(2,10):
    for j in range(1, 10):
        print(i*j, and='')
        print('')