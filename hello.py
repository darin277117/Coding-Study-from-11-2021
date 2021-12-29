# 1번 주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성해 보자.
# def is_odd(num):
#     if num % 2 == 0:
#         return print("홀수")
    
#     else num % 2 == 1:
#         return   print("짝수")
# a = is_odd(2)
# 뭐가 잘못됐을까

# 2번 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자. 
# (단 입력으로 들어오는 수의 개수는 정해져 있지 않다.)

def a(*args):
    result = 0
    for i in args:
        result += i
    return result/len(args)

result = a(1,2,3)
print(result)
# return 함수 위치에 따라 값이 달라짐. 뭘까

# 3과 6을 입력했을 때 9가 아닌 36이라는 결괏값을 돌려주었다. 이 프로그램의 오류를 수정해 보자.
input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")

total = int(input1) + int(input2)
print("두 수의 합은 %s 입니다" % total)