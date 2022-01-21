
def number(n):
    if n == 0: return 0
    if n == 1: return 1
    if n>1: return number(n-2) + number(n-1)

for i in range(0,9):
    print(number(i))