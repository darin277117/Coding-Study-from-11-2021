#1번문제
def is_odd(n):
    if n % 2 == 0:
        print("짝수 입니다.")
    else:
        print("홀수 입니다.")

is_odd(100)

#2번문제
def average_calculate(*n):
    return sum(n)/len(n)

print(average_calculate(1,2,3,4,5,6,7,8))

#3번문제
input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")

total = input1 + input2
print("두 수의 합은 %d 입니다" % int(total))

#4번문제(정답 3번)
print("you" "need" "python")
print("you"+"need"+"python")
print("you", "need", "python")
print("".join(["you", "need", "python"]))

#5번문제
f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("test.txt", 'r')
print(f2.read())

#6번문제
a=input("입력하세요.")
f=open("test2.txt", 'a')
f.write(a)
f.write("\n")
f.close

fr = open("test2.txt", 'r')
print((fr.read()))

#7번 문제(???)
f = open('test.txt', 'r')
body = f.read()
f.close()

body = body.replace('java', 'python')

f = open('test.txt', 'w')
f.write(body)
f.close()
