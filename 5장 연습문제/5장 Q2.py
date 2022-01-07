class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class MaxLimitCalculator(Calculator) :
    def add(self, val) :
        self.value += val
        if self.value > 100 :
            print("100이상은 계산할 수 없습니다.")
            
#이거 실행을 하면 print(cal.value)하기 전에 if문에 있는 print값이 나오는데 혹시 방법 아는사람? 
