data = "4546793"
numbers = list(map(int,data))
result = []

for i, num in enumerate(numbers):
    result.append(str(num))
    if i < len(numbers)-1:                      # 다음 수가 있다면
        is_odd = num%2==1                       # 현재 홀수
        is_next_odd = numbers[i+1] % 2 == 1     # 다음 홀수
        if is_odd and is_next_odd :
            result.append ("-")
        elif not is_odd and not is_next_odd : 
            result.append("*")

print("".join(result))