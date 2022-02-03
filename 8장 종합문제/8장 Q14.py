s=input('문자열을 입력하세요 : ')
num=1
i=1
result=""

while i<=len(s)-1 :
    if s[i-1]==s[i] : # 0과 1자리를 비교
        num+=1
        i+=1
    elif s[i-1]!=s[i] :
        if num!=1 :
            result+=s[i-1] + str(num)
            num=1   
            i+=1
        else :
            result+=s[i-1] + str(num)
            i+=1

result+=s[i-1] + str(num) #마지막 문자열 추가
print(result)