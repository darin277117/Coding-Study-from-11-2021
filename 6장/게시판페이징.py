#m= 게시물의 총 건수, n= 한페이지에 보여지는 개수(10개)
def getTotalPage(m, n =10):
    if m % n == 0:
        return  m // n
    else:
        return m //n +1 

print(getTotalPage(21))

