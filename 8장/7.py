a = []
n = int(input("숫자를 입력해주세요:"))
def gugu(n):
    for i in range(1,10):
        a.append(n*i)
    return a
print(gugu(n))