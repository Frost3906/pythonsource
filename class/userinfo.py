class UserInfo:
    """ 
    UserInfo class
    Author : Park
    Date : 2020.08.12
    Description : Class 작성법
    """

    #Instance method : self를 반드시 인자로 갖고 있어야 한다.
    def user_info(self):
        print("메소드 실행")


#객체 생성
user1 = UserInfo()
user1.user_info()