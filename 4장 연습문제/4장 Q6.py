user_input=input("내용을 입력하세요. : ")
f=open('test.txt','a') #a : 추가모드-파일의 마지막에 새로운 내용을 추가 시킬 때 사용
f.write(user_input)
f.write("\n")
f.close()
