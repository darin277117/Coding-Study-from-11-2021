s=input('문자열을 입력하세요 : ')
num=1
i=1
result=""

while i<len(s) :
    if s[i-1]==s[i] :
        num+=1
        i+=1
    elif s[i-1]!=s[i] :
        result+=s[i-1] + str(num) #num 쓰고 버리기
        num=1   
        i+=1

result+=s[i-1] + str(num)
print(result)
