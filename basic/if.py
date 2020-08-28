#%%
# if 조건문 :
# 실행할 문장
if True:
    print("True")


#%%
a =200
if a< 100:
    print("a는 100보다 작다")
print("조건문에서 들여쓰기는 중요함")

#%%
a = 300
if 200 < a <= 300:
    print("a는 200과 300 사이에 있다")


#%%
a, b, c = 12,6,18
#가장 큰 값 출력

if(a>b):
    if(a>c):
        print(a)
    elif(c>a):
        print(c)
elif(b>a):
    if(b>c):
        print(b)
    elif(c>b):
        print(c)
        
max = a
if max < b:
    max=b
if max < c:
    max = c
print(max)


#%%
#if 조건문:
#   수행문장
#else :
#   수행문장


if True:
    print("True")
else:
    print("False")

#%%
a = 55
if a < 100:
    print("a는 100보다 작다")
else:
    print("a는 100보다 크다")


#%%
score, grade = 90, "A"
if score >= 90 and grade == "A":
    print("합격")
else:
    print("불합격")

#%%
#사용자에게 숫자를 입력받아 그 숫자가 짝수, 홀수인지 판별하기

a = int(input("숫자를 입력해 주세요 :"))
if(a%2==0):
    print("짝수입니다.")
else:
    print("홀수입니다.")


#%%
import datetime
now = datetime.datetime.now()

print(now)
print("{}년 {}월 {}일 {}시 {}분 {}초".format(now.year,now.month,now.day,now.hour,now.minute,now.second))

if now.hour > 12:
    print("오후입니다.")
else :
    print("오전입니다.")

#%%
a = 86
if a >50:
    if a < 100:
        print("50보다 크고 100보다 작다")
    else:
        print("100보다 크다")
else:
    print("50보다 작다")

#%%
score = int(input("점수를 입력하세요 :"))

if score >= 90:
    print("A")
else:
    if(score >=80):
        print("B")
    else:
        if(score >= 70):
            print("C")
        else:
            if(score >= 60):
                print("D")
            else:
                print("F")


num2 = 100
if num2 >= 90:
    print("A")
elif num2 >=80:
    print("B")
elif num2 >= 70:
    print("C")
elif num2 >= 60:
    print("D")
else :
    print("F")



#%%
# 계절 확인: 봄/여름/가을/겨울 중 하나 출력하기

# 3~5 봄, 6~8 여름, 9~11 가을, 12~2 겨울

import datetime
now = (datetime.datetime.now()).month

if(3<=now<=5):
    print("지금은 봄입니다.")
elif(6<=now<=8):
    print("지금은 여름입니다.")
elif(9<=now<=11):
    print("지금은 가을입니다.")
else:
    print("지금은 겨울입니다.")


#%%
#계산기
#두개의 숫자와 연산자를 입력받아 계산한 후 출력하는 프로그램

#+,-,*,/,//,%,**
num1 = int(input("숫자를 입력해 주세요"))
num2 = int(input("하나 더 입력해 주세요"))
op = input("어떤 연산을 하시겠습니까(+ - * / // % **")

if(op=="+"):
    print(num1+num2)
elif(op=="-"):
    print(num1-num2)
elif(op=="*"):
    print(num1*num2)
elif(op=="/"):
    print(num1/num2)
elif(op=="//"):
    print(num1//num2)
elif(op=="%"):
    print(num1%num2)
elif(op=="**"):
    print(num1**num2)


#%%
i = 1
while(i < 11):
    print(i)
    i +=1
print()
i=1
while(i<=10):
    print(i,end=" ")
    i+=1
#%%
#1 ~ 100까지 짝수만 출력
i=1
while(i<101):
    if(i%2==0):
        print(i,end=" ")
    i+=1

#%%
# 1~100 합계 출력
i=1
sum1=0
while i<101:
    sum1+=i
    i+=1
print("1~100까지의 합 : {}".format(sum1))

#%%
#3단 구구단 출력
i=1
while i < 10:
    print("3 * {} = {}".format(i,3*i))
    i+=1

#%%
#사용자로부터 입력받아서 화면에 출력
#종료는 q를 입력하면 종료
data = ""
while data != 'q':
    data = input("입력해 주세요 : ")
    print(data)
    if data =='q':
        print("종료합니다.")
    


