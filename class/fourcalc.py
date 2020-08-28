class FourCal:
    """
    FourCal
    사칙 연산 기능을 가지고 있는 계산기
    두개의 정수를 받아 사칙 연산을 한 후 연산 결과를 리턴하는 4개의 메소드를 작성한다.
    생성자는 두개의 변수를 초기화 하는 형태로 작성하기
    """

    def __init__(self,num1,num2,result = None):
        self.num1 = num1
        self.num2 = num2
        self.result = result
    
    def add(self):
        self.result = self.num1 + self.num2
        return self.result
    def sub(self):
        self.result = self.num1 - self.num2
        return self.result
    def mul(self):
        self.result = self.num1 * self.num2
        return self.result
    def div(self):
        self.result = self.num1 / self.num2
        return self.result



        
a,b = input("두 숫자 입력 : ").split()

a = int(a)
b = int(b)

fourcal = FourCal(a,b)

print("{} + {} = {}".format(fourcal.num1,fourcal.num2,fourcal.add()))
print("{} - {} = {}".format(fourcal.num1,fourcal.num2,fourcal.sub()))
print("{} * {} = {}".format(fourcal.num1,fourcal.num2,fourcal.mul()))
print("{} / {} = {}".format(fourcal.num1,fourcal.num2,fourcal.div()))
