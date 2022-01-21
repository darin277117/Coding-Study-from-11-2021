with open("abc.txt", "r") as f:
    lines = f.readlines() 

lines.reverse()

with open("abc.txt", "w") as f:
    for line in lines:
        line = line.strip()  
        f.write(line)
        f.write('\n')