with open("sample.txt", "r") as f:
    lines = f.readlines( )  
    
total = 0
for line in lines:
    score = int(line)  # 줄에 적힌 점수를 숫자형으로 변환한다.
    total += score
average = total / len(lines)

f = open("result.txt", "w")
f.write(str(average))
f.close()