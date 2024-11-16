'''
str = "89점"
score = int(str)
print(score)

str = '89점'
try:
    score = int(str)
    print(score)
except:
    print('예외가 발생했습니다.')
print('작업 완료')


while True: #무한 반복
    #str = input('점수를 입력하세요 >>>')
    #socre = int(str)
    #print('입력한 점수:', socre)
    str = input('점수를 입력하세요 >>')
    try:
        score = str(int)
        print(score)
    except:
        print('점수 형식이 잘못되었습니다.')
    print('작업 완료')
    break
'''


#str = '89'
#socre = int(str)
#print(score2)
str = '89'
try:
    score = int(str)
    print(score)
    a = str[3]
except NameError:
    print('점수 형식이 잘못되었습니다.')
except NameError:
    print('리스트변수의 첨자위를 확인하세요')