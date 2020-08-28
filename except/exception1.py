#예외상황
# 컴파일 예외 -> 문법적인 에러
# 런타임 예외 => 실행 후에 나타나는 에러

#%%
print("Test")
a,b = 10,15
#print(c) #NameError : 참조 변수 없음


# %%
print(10/0) #ZeroDivisionError
# %%
list = [10,20,30]
print(list[0])
print(list[3]) #IndexError
# %%
dict = {"name":"Kim","age":25,"city":"seoul"}
#print(dict["hobby"]) #KeyError
print(dict.get("hobby"))  #None

# %%
x=[1,5,9]
#x.remove(10) #ValueError: list.remove(x): x not in list
x.index(10) #ValueError: 10 is not in list
# %%
number_input = int(input("정수 입력 >>")) #ValueError: invalid literal for int() with base 10: '3cm'
print("원 반지름 : ", number_input)
print("원 둘레 : ",2*3.14*number_input)
print("원 넓이 : ",3.14*number_input*number_input)
# %%
x = [1,2] #리스트
y = (3,4) #튜플

print(x+y) #TypeError: can only concatenate list (not "tuple") to list
