# 3 의 배수의 합 + 5의 배수의합 - 15의 배수의 합

a=0
for n in range(1, 1000):
    if n % 3 ==0:
        a += n
    if n % 5 ==0:
        a += n
    if n % 15 ==0:
        a -= n

print(a)