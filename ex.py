#1번 문제(이거 맨처음 밖에 안나오나?)
a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")

#2번 문제
x=1
k = []
while x<1000:
    x= x+1
    if x % 3 ==0:
        k.append(x)
        
print(sum(k))

#3번 문제
a=0
while a < 5:
    a = a+1
    print("*"*a)

#4번 문제
k=[]
a=1
while a < 100:
    a = a + 1
    k.append(a)

for i in k:
    print(i)    

#5번 문제
l=[70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total=0
for i in l:
   total += i

average= total / len(l)
print(average)

#6번 문제 리스트 내포가 뭐임?
numbers = [1, 2, 3, 4, 5]
result=[a*2 for a in numbers if a % 2 ==1]
print(result)
