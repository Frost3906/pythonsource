#%%
# A:90, B:80, C:70 의 형태를 dict 구조로 생성한 후 key:value 형태로 출력

Q1={"A":90,"B":80,"C":70}
print(Q1)



# %%
# B 키값을 삭제한 후 전체 dict 출력
del Q1["B"]
print(Q1)


# %%
#다음 항목을 dict로 생성하기
#성인 - 10000, 청소년 - 7000, 아동 - 3000
dict3 = {"성인":10000, "청소년":7000, "아동":3000}

# %%
#위에서 선언한 dict에 소아 - 0 항목 추가한 후 출력
dict3["소아"] = 0
print(dict3)


# %%
#위에서 선언한 dict의 key 값만 출력
print(dict3.keys())


# %%
# foods 라는 딕셔너리를 생성하고 각 음식에 맞는 value를 출력하기
foods ={
    "떡볶이":"오뎅",
    "짜장면":"탕수육",
    "치킨":"맥주",
    "삼겹살":"소주",
    "피자":"스파게티",
    "라면":"김밥"
}
#사용자에게 좋아하는 음식을 고르게 한 후 음식과 궁합이 맍는 음식 출력

#입력값이 '끝'인 경우 반복문 종료
#키 값에 없는 음식을 고르면 "다른 음식을 선택해 주세요" 출력
#input(str(list(foods.keys())+" 중 좋아하는 것은?")
while 1:
    # food1 = input("좋아하는 음식을 고르세요 : ")
    food1 = input(str(list(foods.keys()))+" 중 좋아하는 것은?")
    if food1 in foods:
        print(foods.get(food1))

    elif food1=='끝':
        print("프로그램을 종료합니다.")
        break
    else :
        print("다른 음식을 선택해 주세요")



