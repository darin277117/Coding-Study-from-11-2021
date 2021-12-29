#다음과 같은 내용을 지닌 파일 test.txt가 있다. 이 파일의 내용 중 "java"라는 문자열을 "python"으로 바꾸어서 저장해 보자.

#Life is too short
#you need java




f1 = open("test.txt",'w')
f1.write("Life is too short\n")
f1.write("you need java")
f1.close()
f2 = open("test.txt",'r')
a = f2.read()
f2.close()
a = a.replace("java","python")
f3 = open("test.txt", 'w')
f3.write(a)
f3.close()