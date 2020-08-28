class UserInfo:
    """ 
    UserInfo class
    Author : Park
    Date : 2020.08.12
    Description : Class 작성법 / 인자 있는 생성자 / 클래스 변수

    """

    user_count = 0


    #생성자 : 생성자 오버로딩 개념 없음
    def __init__(self,name,age):
        self.name= name
        self.age = age
        UserInfo.user_count +=1


    #Instance method : self를 반드시 인자로 갖고 있어야 한다.
    def user_info(self):
        print("메소드 실행")

    def __str__(self):
        return "name : {}, age : {}".format(self.name,self.age)

    def __del__(self):
        UserInfo.user_count -= 1


#객체 생성
user1 = UserInfo("홍길동",25)
user2 = UserInfo("성춘향",26)

#메소드 호출
user1.user_info()

print(user1)
print(user2.__dict__)

print()


print("생성된 User : {}명".format(UserInfo.user_count))
print("생성된 User : {}명".format(user1.user_count))
print("생성된 User : {}명".format(user2.user_count))


#객체 생성
del user1
print("삭제 된 후 User: {}명".format(UserInfo.user_count))