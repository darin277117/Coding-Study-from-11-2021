dictionary = {1:1, 2:1}
def pivonacci(n):
    if n in dictionary:
        return dictionary[n]
    else:
        output = fibonacci(n-1) + fibonacci(n-2)
        dictionary[n] = output
        return output

print(input("원하는 숫자를 입력하세요"))
   

