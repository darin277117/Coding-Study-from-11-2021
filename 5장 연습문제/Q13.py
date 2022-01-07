import random
a = 0
result = []
while a<6:
    a += 1
    number = random.randint(1,45)
    result.append(number)
    if number == number:
        continue
print(result)
#lotto = sorted(random.sample(range(1,46),6))
#print(lotto)    
