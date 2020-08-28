# 파이썬 데이터 타입
# 정수형
# 문자형 : '',"" 둘 다 허용, '''.... ''', """..."""

#%%
a = "Life is too short, You need Python"
a = """\
    여러줄 표현시 사용
    Life is too short, You need Python
"""
print(a)


#%% 문자열 응용
# + : 결합
print("Python " + "is Fun")

# * : 복제
print("파이썬" * 2)


#%%
print("*" * 50)
print("My Program")
print("*" * 50)

#%% 인덱싱

str1 = "Life is too short"
print("str1[3]", str1[3])  # 기준 : 왼쪽
print("str1[-3]", str1[-3])  # 기준 : 오른쪽

#%%
# 슬라이싱 - 중요도 높음
print("str1[0:4]", str1[0:4])  # Life
print("str1[5:7]", str1[5:7])  # is
print("str1[8:11]", str1[8:11])  # too
print("str1[0:-4]", str1[0:-4])  # Life is too s
print("str1[:]", str1[:])  # 전체 문자열
print("str1[:17]", str1[:17])
print("str1[4:]", str1[4:])

#%%
# 문자열 길이 len()
print(len(str1))


#%%
str2 = "20200804Rainny"

# 20200804
date = str2[:8]
print(date)
# Rainny
weather = str2[8:]
print(weather)

# 2020-08-04
year = date[:4]
month = date[4:6]
day = date[6:]
print(year, month, day, sep="-")


# %%
#주민등록번호에서 8자리 숫자 사용해서 남자,여자 판별
#1,3 -> 남 / 2,4 -> 여

str1 = "940309-1034724"
no=str1[7] 
if(no=='1' or no=='3'):
    print('남자')
elif(no=='2'or no=='4'):
    print('여자')


# %%
#각 문자 끝에 $찍기
str1 = '대한민국'
for s in str1:
    print(s+'$',end="")

# %%
no = input('숫자를 입력하세요 : ')
for j in range(len(no)):
    for i in range(int(no[j])):
        print('★',end="")
    print()




# %%
#문자열 관련함수 -1. count : 문자열에 포함된 특정 문자열의 개수
str1 = 'hobby'
print('str1에 포함된 b 문자열 개수 : ',str1.count('b'))

# %%
#문자열 관련 함수 -2.find : 문자열 찾기
str1 = "Python is best Choice"
print("b가 시작되는 첫번째 위치 : ", str1.find('b')) 
print("b가 시작되는 첫번째 위치 : ", str1.find('z')) #없는 것은 -1을 돌려줌

print("b가 시작되는 첫번째 위치 : ", str1.find('o',6)) # 6번째 이후로 o가 시작되는 위치 

# %%
print("b가 시작되는 첫번째 위치 : ", str1.index('b')) 
print("b가 시작되는 첫번째 위치 : ", str1.index('k')) #error

print("b가 시작되는 첫번째 위치 : ", str1.index('o',6)) # 6번째 이후로 o가 시작되는 위치 


# %%
# 문자열 관련 함수 -3. startswith / endswith : 특정 문자열로 시작 혹은 끝나는지 확인
str1 = "Python is best Choice"
print(str1.startswith("P")) # True or False
print(str1.endswith("x")) # True or False


# %%
# 문자열 관련함수 -5. join : 문자열 연결
a=","
print("문자열 연결",a.join('abcde'))
print('a','b','c','d','e',sep=a)
#리스트를 일반 문자열로 변경할 때 주로 쓰임
#" ".join(list) 형태로 쓰임


# %%

#문자열 관련 함수 6. upper / lower : 대문자 혹은 소문자로 변경
str1 = 'abcde'
print("대문자로 변경 : ",str1.upper())
str2 = str1.upper()
print(str2)
print("소문자로 변경 : ",str2.lower())

# %%
# 문자열 관련 함수 -7. swapcase : 대소문자 상호 변환
str1 = "Python is best Choice"
print(str1.swapcase())


# %%
#문자열 관련 함수 -8. title : 단어의 첫글자만 대문자로
str1 = "python is easy"
print(str1.title())



# %%
# 문자열 관련 함수 -9. strip / lstrip / rstrip : 공백 제거
str1 = "         hi"
print(str1.strip()) #양쪽 공백 제거
print(str1.lstrip()) #왼쪽 공백 제거
print()
str1 = "hi              "
print(str1.strip())
print(str1.rstrip()) # 오른쪽 공백 제거
print()
str1 = "             hi              "
print(str1.strip())


# %%
# 문자열 관련 함수 - 10. replace : 문자열 바꾸기
str1 = 'Life is too short'
print(str1.replace("Life","Your leg"))

# %%
# 문자열 관련 함수 11.split : 특정 문자로 문자열 나누기 / list의 형태로 반환됨
print(str1.split())
str1 = "Life:is:too:short"
print(str1.split(':'))
str1 = "Life\nis\ntoo\nshort"
print(str1.splitlines())
print(" ".join(str1.splitlines()))
#join : 리스트를 일반 문자열로 변경할 때 주로 쓰임
#" ".join(list) 형태로 쓰임


# %%
# 문자열 관련 함수  -12. center / ljust / rjust / zfill - 문자열 정렬
str1 = "파이썬"
print(str1.center(10,"*"))
print(str1.ljust(10,"*"))
print(str1.rjust(10,"*"))
print(str1.zfill(10)) #빈공간은 0으로 채움

# %%
# 문자열 관련함수 - 13. 문자열 구성 파악
print('1234'.isdigit())
print('abcd'.isalpha())
print('abc123'.isalnum())
print('abcd'.islower())
print('ABCD'.isupper())
print('    '.isspace())

# %%
# 대문자는 소문자로 소문자는 대문자로 변경 후 출력하기
# name = "KennRY" swapcase() 사용하지 않고
name = input("영문이름을 입력하십시오")
for i in name:
    if(i.isupper()):
        print(i.lower(),end="")
    else:
        print(i.upper(),end="")

# %%
# 사용자로부터 년/ 월 / 일 형태의 데이터를 입력 받고 10년 후의 날짜를 출력
# 입력값 2020/08/05 => 2030년 08월 05일
date1 = input("년/월/일 입력 : ").split("/")
year = int(date1[0])
month = int(date1[1])
day = int(date1[2])
print("{}년 {}월 {}일".format(year+10,month,day))

# %%
# 웹 사이트 주소를 이용한 비밀번호 생성하기
# https://naver.com => nav51!
# 규칙 1 : https:// 이부분은 제외
# 규칙 2 : 처음 만나는 점(.) 이후의 부분은 제외 => com 제외
# 규칙 3 : 남은 글자 중 처음 세자리 + 글자갯수 + 글자 내 'e'갯수 + "!" 구성

url = input("사이트 주소 입력 : ")
word = url[url.find(':')+3:url.find('.')]
password = word[0:3]+str(len(word))+str(word.count('e'))+'!'
print(password)
print(url[url.find(':')+3:url.find('.')])
