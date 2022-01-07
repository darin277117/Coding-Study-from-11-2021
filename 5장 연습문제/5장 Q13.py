import random
data=[]

while len(data) < 6 :
    n = random.randint(1,45)
    if n not in data :
        data.append(n)

print(data)
