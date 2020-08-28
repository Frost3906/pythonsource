class UserInfo:
    """ 
    UserInfo class
    Author : Park
    Date : 2020.08.12
    Description : Class 작성법 / 인자 있는 생성자

    """
    #생성자 : 생성자 오버로딩 개념 없음
    def __init__(self,name,age):
        self.name= name
        self.age = age


    #Instance method : self를 반드시 인자로 갖고 있어야 한다.
    def user_info(self):
        print("메소드 실행")

    def __str__(self):
        return "name : {}, age : {}".format(self.name,self.age)


#객체 생성
user1 = UserInfo("홍길동",25)
user2 = UserInfo("성춘향",26)

#메소드 호출
user1.user_info()

print(user1)
print(user2.__dict__)
