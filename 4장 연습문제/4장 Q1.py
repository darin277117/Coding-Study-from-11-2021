num=int(input("숫자입력 : "))


def is_odd(num) :
    if num%2==0 :
        return '짝수'
    else :
        return '홀수'

print(is_odd(num))
