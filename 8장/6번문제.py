# 그대로 붙여넣어(65,45,2,3,45,8) 괄호빼고
user_input = input("주석의 숫자를 입력하세요.(괄호제외)")
a = user_input.split(",")

total = 0
for i in a:
    total += int(i)

print(total) 