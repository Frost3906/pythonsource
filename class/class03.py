#클래스가 필요한 이유

# 학생 3명의 정보를 다룬다면?

# 학생 : 이름, 학번, 학년, 성별, 점수1, 점수2


student_dict = [
    {
        "student_name":"Kim",
        "student_number":1,
        "student_grade":1,
        "student_detail":{"gender":"male", "score1":95,"score2":88}
        },

    {
        "student_name":"park",
        "student_number":2,
        "student_grade":2,
        "student_detail":{"gender":"female", "score1":78,"score2":55}
        },
    {
        "student_name":"cho",
        "student_number":3,
        "student_grade":3,
        "student_detail":{"gender":"male", "score1":47,"score2":83}
        }
]



#학생1
#이름리스트 생성
student_name_list = ['kim','park','cho']
student_number_list = [1,2,3]
student_grade_list = [1,2,3]
student_detail_list =[
{"gender":"male", "score1":95,"score2":88},
{"gender":"female", "score1":78,"score2":55},
{"gender":"male", "score1":47,"score2":83}
]

# print(student_name_list)
# print(student_number_list)
# print(student_grade_list)
# print(student_detail_list)

for i in range(3):
    print(student_name_list[i],student_number_list[i],student_grade_list[i],student_detail_list[i])
