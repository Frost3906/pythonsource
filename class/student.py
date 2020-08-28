# 기본적 개념은 public
class Student(): #()는 필수요소가 아님
    def __init__(self,name, number, grade, details): # self 반드시 존재
        self.name=name
        self.number = number
        self.grade = grade
        self.details = details
    
    def __str__(self): #toString 기능
        return "{},{},{},{}".format(self.name,self.number,self.grade,self.details)

#객체 생성
student1 = Student("홍길동",1,1,{"gender":"female", "score1":78,"score2":55})
student2 = Student("이씨",2,2,{"gender":"male", "score1":87,"score2":24})
student3 = Student("김씨",3,3,{"gender":"fale", "score1":156,"score2":25})


# __dict__ : 클래스 인스턴스 값 확인 시 사용
print(student1.__dict__)
print(student2.__dict__)
print(student3.__dict__)

