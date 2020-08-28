#%%
# q1) A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는
#     다음과 같다. A 학급의 평균을 구하시오
#     70,60,55,75,95,90,80,85,100
#     [조건] 중간고사 점수를 리스트로 생성하고 평균 구하기
q1 = [70,60,55,75,95,90,80,85,100]
print(sum(q1)/len(q1))




#%%
# q2) 아래 문자열의 길이를 구하시오.
q2 = "dk2jd23iljdk2jd93fdkedieliddkfiejfied"
print("문자열의 길이 : ",len(q2))


#%%
# q3) 화면에 * 기호 100개를 표시하기
print('*'*100)
#%%
# q4) 문자열 30을 각각 정수형, 실수형, 문자형으로 변경해서 출력하기
q4="30"
print("정수형 : ", int(q4))
print("실수형 : ", float(q4))
print("문자형 : ", '"30"')



#%%
# q5) 문자열 Niceman 에서 man 문자열만 출력하기
q5 = "Niceman"
print(q5[-3:])

#%%
# q6) 문자열 http://www.daum.net 에서 http:// 제거하고 출력하기
q6 = "http://www.daum.net "
print(q6[q6.find(':')+3:])

#%%
# q7) 문자열 abcdefghijklmn 에서 슬라이싱을 이용해 "cde" 만 출력하기
q7 = "abcdefghijklmn"
print(q7[2:5])

#%%
# q8) 다음 리스트에서 "Apple" 항목만 삭제하고 출력하기
q8 = ["Banana","Apple","Orange","Grape"]
q8.remove("Apple")
print(q8)

#%%
# q9) 다음 리스트에서 '정' 글자만 제외하고 출력하기
q9 = ["갑","을","병","정","경"]
for i in q9:
    if(i=="정"):
        continue
    print(i,end=" ")


print("\n -- comprehension --")
q9_2 = [str1 for str1 in q9 if str1 !='정']
print(q9_2)

#%%
# q10) 다음 리스트에서 5글자 이상의 단어만 출력하기
q10 =["nice","study","python","anaconda","!"]
for i in q10:
    if(len(i)>=5):
        print(i)
print("\n-- comprehension --")
q10_2 = [str1 for str1 in q10 if len(str1)>=5]
print(q10_2)
#%%
# q11) 아래 리스트에서 소문자만 출력하기
q11 = ["A","b","c","D","e","F","G","h"]
for i in q11:
    if(i.islower()):
        print(i, end=" ")
print("\n-- comprehension --")
q11_2 = [str1 for str1 in q11 if str1.islower()]
print(q11_2)

#%%
# q12) 아래 리스트에서 소문자는 대문자로 대문자는 소문자로 출력하기
q12 = ["A","b","c","D","e","F","G","h"]
for i in q12:
    print(i.swapcase(),end=" ")

#%%
# q13) 주차장 프로그램 작성하기
list1=[]
choice = 0
car = 'A'
i=1
print('='*50)
while 1:
    print('[1] 자동차 넣기 | [2] 자동차 빼기 | [3] 종료 :')
    choice = input()
    if choice == '1':
        if(len(list1)<5):
            print(car+" 차량 들어옴. 주차장 상태",end=" ")
            list1.append(car)
            car = chr(ord(car)+1)
            print(list1)
        else :
            print("주차장 가득 참")
    elif choice =='2':
        if(len(list1)>0):
            print(list1[-1]+" 차량 나감. 주차장 상태",end=" ")
            list1.pop()
            print(list1)
        else:
            print('주차장 텅 빔')
    elif choice =='3':
        print('프로그램 종료')
        break
    else:
        print("잘못된 접근입니다. 다시 입력해 주세요")
    




# %%
print(chr(ord(car)+1))
