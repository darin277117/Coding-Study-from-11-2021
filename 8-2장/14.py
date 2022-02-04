#'''
# 문자열 압축하기
# 문자열을 입력받아 같은 문자가 연속적으로 반복되는 경우에 그 반복 횟수를 표시해 문자열을 압축하여 
# 표시하시오.
# 어떻게 풀지? 우선 리스트로 받아.
# 입력 예시: aaabbcccccca
# 출력 예시: a3b2c6a1
# 1. 리스트 내에서 요소 개수 샌것을 변수로 받아.
# 손코딩 개꿀
# '''
lst=list("aaabbcccccca")
ac=str(lst.count("a"))
bc=str(lst.count("b"))
cc=str(lst.count("c"))
print("a"+ac+"b"+bc+"c"+cc+"a")