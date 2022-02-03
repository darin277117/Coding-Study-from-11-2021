numbers=[]
s=input("숫자를 입력하세요. (0~9만 사용, 공백으로 구분) :")
numbers=s.split()
all_numbers="0123456789"
n=0

for i in numbers :
    new_numbers=sorted(list(set(i)))
    new_check=sorted(list(i))
    print(new_check)