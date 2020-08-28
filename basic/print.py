# print 함수
print('Hello Python!') # ' ' : 문자열 <class 'str'>
print("Hello Python!") 
print(100)  # <class 'int'>
print("100")
print(24.562) #<class 'float'>
print()
print(True) # bool 타입 = True, False

print("""안녕""") #'''안녕'''
print('T','E','S','T') # T E S T

# print 옵션
# sep : 각 문자열의 구분을 무엇으로 할 것인가 지정
print('T','E','S','T', sep="") # TEST
print('T','E','S','T', sep=",") # T,E,S,T
print('2020','07','31', sep="-") # 2020-07-31
print('ㅁㄴㅇㄻㄴㄹ','ㅁㄴㅇㄻㄴㅇㄹ', sep="@") # ㅁㄴㅇㄻㄴㄹ@ㅁㄴㅇㄻㄴㅇㄹ

# end : 해당 옵션이 없는 경우 print() 무조건 한줄 출력
#       옵션을 줘서 공백을 표시해주면 다음 라인과 연결

print("Welcome To ", end="")
print("Python World")


