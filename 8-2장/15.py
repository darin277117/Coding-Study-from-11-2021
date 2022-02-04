# 리스트내에서 갯수가 2개 이상이면 False 출력하면 되게 한다.
a=list("0123456789") 
b=list("01234") 
c=list("0123456780") 
d=list("6789012345")
e=list("01232245679")
if len(a) == len(set(a)):
    print("True")
else:
    print("False")

if len(b) == len(set(b)):
    print("True")
else:
    print("False")    

if len(c) == len(set(c)):
    print("True")
else:
    print("False")

if len(d) == len(set(d)):
    print("True")
else:
    print("False")

if len(e) == len(set(e)):
    print("True")
else:
    print("False")