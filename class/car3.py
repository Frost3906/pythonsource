class Car:
    # #인스턴스 변수
    # color = ""
    # speed = 0

    def __init__(self,color,speed):
        self.color = color
        self.speed = speed

    def upSpeed(self, value):
        self.speed += value
    
    def downSpeed(self, value):
        self.speed -= value

#객체 생성
myCar1 = Car("Red",30)

myCar2 = Car("Blue",20)

myCar3 = Car("Black",50)

myCar1.upSpeed(20)
print("자동차1의 색상은 {}이며 현재 속도는 {:3d}km".format(myCar1.color,myCar1.speed))
myCar2.upSpeed(10)
print("자동차2의 색상은 {}이며 현재 속도는 {:3d}km".format(myCar2.color,myCar2.speed))
myCar3.upSpeed(30)
print("자동차3의 색상은 {}이며 현재 속도는 {:3d}km".format(myCar3.color,myCar3.speed))

print()
print("myCar1 주소 : ",id(myCar1))
print("myCar2 주소 : ",id(myCar2))
print("myCar3 주소 : ",id(myCar3))


print()
