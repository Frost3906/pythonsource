#%%
# key, value
# 순서 없음, 중복 안됨, 수정, 삭제 가능

dict1 = {"name": "Park", "age": 12}
print(dict1)

dict2 = {0:"Hello", 1:"Python", 3:"Coding"}
print(dict2)

dict3 = {"arr":[1,2,3,4,5]}
print(dict3)

dict4 = {"arr":(1,2,3,4,5)}
print(dict4)

# %%
# dict에서 특정 키의 값을 출력하기
# get() : 없는 키 값일때 None으로 돌려줌
print(dict1["name"])
print(dict1["addr"])


# %% 내용 추가하기
dict1["birth"] = "1234"
print(dict1)

dict2[3] = [4,5,6]
print(dict2)

dict4["test"] = (8,9,10)
print(dict4)

#%% 삭제
del dict1["birth"]
print(dict1)

# %% dict key 값 가져오기
print(dict1.keys())
print(dict2.keys())
print(dict3.keys())
print(dict4.keys())






# %% dict value 값 가져오기
print(dict1.values())
print(dict2.values())
print(dict3.values())
print(dict4.values())

# %% key,value 형태
print(dict1.items())
print(dict2.items())
print(dict3.items())
print(dict4.items())



# %% 해당 키가 딕셔너리 안에 있는지 확인
print("name" in dict1)
print(5 in dict2)

# %% dict 안의 모든 값 지우기
dict1.clear()
print(dict1)


# %%
myInfo = {"name": "kim", "age":24, "city":"seoul"}
for k in myInfo.keys():
    print(k,end=" ")
print()
for v in myInfo.values():
    print(v,end=" ")
print()
for k,v in myInfo.items():
    print(k,v)



# %%
#4 계절을 대표하는 과일을 dict 구조로 생성
fruits = {"봄":"봄", "여름":"여름", "가을":"가을과일", "겨울":"사과"}
#가을의 과일이 무엇인지 출력하기
print(fruits["가을"])

#사과가 포함되어있는지 확인하기
print("사과" in fruits)




# %%
# comprehension
fruit = {f for f in fruits.values()}
print(fruit)

fruit = {f for f in fruits.values() if f != "사과"}
print(fruit)

fruit = {(k,v) for (k,v) in fruits.items()}
print(fruit)