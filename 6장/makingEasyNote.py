#"""" 이 문제 해설이 이해가 안감. 그래서 그냥 파일 열고 쓰고닫기만함.
#2. memo.py를 작성했다면 다음 명령을 수행해 보자.""""

#원하는 메모를 파일에 저장하고 추가 및 조회가 가능한 간단한 메모장을 만들어 보자.
file = open("ex.txt", "w")
file.write("아 이 문제 해설 왤캐 이해가 안가냐")
file.write("\n")

file.close()


#더 무엇인가를 쓰고 싶을떄
with open("ex.txt", "a") as file:
    file.write(input())