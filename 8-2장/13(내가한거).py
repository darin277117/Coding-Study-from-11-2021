#"""Dash insert 함수만들기, 홀수연속 - 짝수연속* 추가
# 어떻게 풀까?
# 연속하는 얘들이 홀수 연속인지 짝수 연속인지 어떻게알지?
# 홀수 * 홀수 = 홀수-->-기호, 짝수 + 짝수 = 짝수 and 짝수 * 짝수 = 짝수인경우엔-->*기호추가
# 함수선언해서 숫자를 받아야됨.
# 반복을 돌려서 연속인지 아닌지 알아야 됨
# 4546793
# 454*67-9-3 str(n)
# """
def dash_insert(n):
    a = list(map(int,str(n)))
    result=[]
    for i in range(len(a)-1):
        if int(a[i]) + int(a[i+1]) % 2 == 0 and int(a[i]) * int(a[i+1]) % 2 ==0:#연속하는 숫자가 짝수
            result.append(str(a[i]) + "*"+ str(a[i+1]))
        if int(a[i]) * int(a[i+1]) % 2 ==1: #홀수 * 홀수 --> 홀수, 즉 연속하는 숫자가 홀수일떄
            result.append(str(a[i]) + "-"+ str(a[i+1]))
        else:
            result.append(str(a[i]))
       
    print(result)
   

dash_insert(4546793)
