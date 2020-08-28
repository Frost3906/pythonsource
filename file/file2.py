# 파일 읽기



#%%
f = open("./resource/test1.txt","r",encoding="utf-8")
print(f.read())
f.close()
# %%
with open("./resource/test1.txt","r",encoding="utf-8") as f:
    print(f.read())

# %%
with open("./resource/review.txt","r",encoding="utf-8") as f:
    print(f.read())

# %%
with open("./resource/review.txt","r",encoding="utf-8") as f:
    for c in f:
        print(c.strip())
# %% readline() 줄단위로 읽어오기
with open("./resource/review.txt","r",encoding="utf-8") as f:
    #print(f.readline())
    line = f.readline()
    while line:
        print(line,end="")
        line=f.readline()

# %%
with open("./resource/review.txt","r",encoding="utf-8") as f:
    print(f.readlines())
# %%
with open("./resource/review.txt","r",encoding="utf-8") as f:
    content = f.readlines()
    for c in content:
        print(c, end="")

# %%
#score.txt 평균을 구한 후 화면에 출력
with open("../resource/score.txt","r",encoding="utf-8") as f:
    score = []
    for num in f:
        score.append(int(num))

print("평균 : ",sum(score) / len(score) )
print("평균 : %.2f" % (sum(score)/len(score)))


# %% score.txt 읽어와서 총합과 평균을 구한 후 구한 결과값을 result.txt 쓰기
with open("../resource/score.txt","r",encoding="utf-8") as f:
    score = []
    for num in f:
        score.append(int(num))

with open("../resource/result.txt","w",encoding="utf-8") as f:
    f.write("총합 : %d\n" % sum(score))
    f.write("평균 : %.2f\n" % (sum(score)/len(score)))




# %% 특정 경로의 파일을 읽어서 사용자가 지정하는 폴더로 복사
# os.path.exists("D:/temp/test.txt")
import os #운영체제와 관련된 기능을 가진 모듈(폴더생성, 폴더 목록 보기)
content = ""
#사용자에게 읽을 파일을 입력받고 저장할 폴더와 이름도 입력 받기
fName = input("읽어 올 파일명을 입력하세요 ")
if(os.path.exists(fName)):
    with open(fName, "r", encoding="utf-8") as inFp:
        content = inFp.read()

    oName = input("저장할 폴더와 이름을 입력하세요")
    with open(oName, "w", encoding="utf-8") as outFp:
        outFp.writelines(content)
else:
    print("%s 파일이 없습니다." %fName)
#파일이 존재하면 읽은 후 사용자가 입력한 저장 폴더에 읽은 파일을 저장

#%%
#info.txt 파일을 읽어 BMI 지수를 계산한 후 화면에 출력하기
#bmi 지수 = 체중 / (키/100)**2
#bmi 지수가 25 이상이면 과체중, 18.5이상이면 정상체중 미만이면 저체중
# 출력결과
# 이름 : 
# 몸무게 :
# 키 :
# BMI :
# 결과 :

with open("../resource/info.txt", "r", encoding="utf-8") as info:
    for i in info.read().split("\n"):
        name = i.split(",")[0]
        height = int(i.split(",")[1])
        weight = int(i.split(",")[2])
        BMI = (weight/((height/100)**2))
        print("이름 : {}".format(name))
        print("몸무게 : {}".format(weight))
        print("키 : {}".format(height))
        print("BMI : %.2f" % BMI)
        if(BMI > 25):
            print("결과 : 과체중")
        elif(BMI >= 18.5):
            print("결과 : 정상체중")
        else:
            print("결고 : 저체중")
        print()

#%% 이진파일
data = ""
try :
    with open("c:/windows/notepad.exe","rb") as f1:
        data = f1.read()
    
    with open("c:/temp/notepad.exe","wb") as f2:
        f2.write(data)
except:
    print("복사 실패")