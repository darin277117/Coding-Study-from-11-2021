#Q1.
#주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성해 보자.
def is_odd(a):
    if a % 2 == 1:
      return "a는 홀수이다."
    else:
      return  "a는 짝수이다."

print(is_odd(3))
