class UserInfo:
    """ 
    UserInfo class
    Author : Park
    Date : 2020.08.12
    Description : Class 작성법 / 생성자 

    """
    #생성자 : 생성자 오버로딩 개념 없음
    def __init__(self, name, age=None, email=None):
        self.name= name
        self.age = age
        self.email= email


    #Instance method : self를 반드시 인자로 갖고 있어야 한다.
    def user_info(self):
        print("메소드 실행")

    def __str__(self):
        return "name : {}, age : {}, email={}".format(self.name, self.age, self.email)


#객체 생성
user1 = UserInfo("사람")
user2 = UserInfo("사람",23)
user3 = UserInfo("사람2",25,'이메일@이메일')
print(user1.__str__())
print(user2.__str__())
print(user3.__str__())
