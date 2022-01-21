tot = 0
f = open('sample.txt','r')
lines = f.readlines()
for line in lines:    
    line = line.strip()
    num = int(line)
    
    tot += num 
average = tot/len(lines)
print(tot)
print(average)
f.close()

f = open('result.txt', 'w')

f.write(str(average))
f.close()
