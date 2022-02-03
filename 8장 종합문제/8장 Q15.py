numbers=[]
s=input("숫자를 입력하세요. (0~9만 사용, 공백으로 구분) :")
numbers=s.split()

def checkpoint(numbers) :
    all_numbers=['0','1','2','3','4','5','6','7','8','9']
    result=""
    n=0

    for i in numbers :
        new_check=sorted(list(i))
        if new_check==all_numbers :
            result+="True "
            n+=1
        else :
            result+="False "
            n+=1
    return result

print(checkpoint(numbers))