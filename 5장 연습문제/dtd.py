class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class MaxLimitCalculator(Calculator) :
    def add(self, val) :
        self.value += val
        data=["100이상은 계산할 수 없습니다."]
        if self.value > 100 :
            self.value=data

cal = MaxLimitCalculator()
