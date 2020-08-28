class Account:
    """
    은행계좌 클래스
    계좌번호, 이름, 잔액을 받아서 객체 생성
    입급 / 출금 기능의 메소드 구현
    """

    def __init__(self,accId,name,total):
        self.accId= accId
        self.name = name
        self.total = total
        
    def save(self,amount):
        self.total += amount
        print("입금 후 잔액 :",self.total)
    def withdraw(self,amount):
        self.total -+ amount
        print("출금 후 잔액 :",self.total)

a = input("생성할 계좌번호를 입력 : ")
b = input("성함을 입력 : ")
c = int(input("잔액을 입력 : "))

myAccount = Account(a,b,c)

print("현재 잔액 :",myAccount.total)
myAccount.save(1000)
myAccount.withdraw(1000)
