import random

result = []
while len(result)<6:
    number = random.randint(1,45)
    if number in result :
        continue
    else: 
        result.append(number)

print(result)
