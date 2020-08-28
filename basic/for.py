#%%
# range() : 범위지정

print(range(5)) #0 ~ 5

print(list(range(5))) #[0,1,2,3,4]

print(list(range(1,5))) #[1,2,3,4]

print(list(range(0,10,2))) #[0,2,4,6,8]


 


# %%
# 0 ~ 9 출력
for i in range(1,11):
    print(i)

# %%
# 1 ~ 100 옆으로 출력
for i in range(1,101):
    print(i,end=" ")

# %%
# 1~10 짝수
for i in range(2,11,2):
    print(i)


# %%
#1 ~ 100 합계 출력
sum1=0
for i in range(1,101):
    sum1 += i
print(sum1)    

# %%
# 1~사용자가 입력한 숫자까지 합계 출력
max = int(input())
sum1 = 0
for i in range(1,max+1):
    sum1 += i
print(sum1)

# %%
for i in range(4,-1,-1):
    print(i)


# %%
print(sum(range(1,11)))

# %%
word = 'dreams'
for s in word:
    print(s)

# %%
# 3단 출력
for i in range(3):
    for j in range(3):
        for k in range(3):
            print(k, end=" ")
        print()
    print()

# %%
#0 1 2 3 4
#1 2 3 4 5
#2 3 4 5 6
#3 4 5 6 7
#4 5 6 7 8
for i in range(5):
    for j in range(5):
        print(j+i, end=" ")
    print()


# %% 2~9단 출력
for i in range(2,10):
    for j in range(1,10):
        print("%d * %d = %d" %(i,j,i*j),end="\t")
    print()

#%%
for i in range(1,10):
    for j in range(2,10):
        print("%d * %d = %d" %(j,i,i*j),end="\t")
    print()

# %%
i = 1
while i <= 10:
    if i == 5:
        break
    print(i, end=" ")
    i+=1

# %%
i = 1
while i <= 10:
    i += 1
    if i%2==1:
        continue
    print(i,end=" ")

# %%
# 1 ~ 10출력 5 제외
for i in range (1, 11):
    if(i==5):
        continue
    else:
        print(i)


# %%
for i in range(6):
    for j in range(i):
        print('*',end="")
    print()
        

# %%
