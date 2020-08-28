#클래스가 필요한 이유

# 학생 3명의 정보를 다룬다면?

# 학생 : 이름, 학번, 학년, 성별, 점수1, 점수2

#학생1
student_name_1 = "Kim"
student_number_1 = 1
student_grade_1 = 1
student_detail_1 = [{"gender":"male"}, {"score1":95},{"score2":88}]

#학생2
student_name_2 = "Park"
student_number_2 = 12
student_grade_2 = 1
student_detail_2 = [{"gender":"female"}, {"score1":78},{"score2":55}]

#학생3
student_name_3 = "Hong"
student_number_3 = 32
student_grade_3 = 1
student_detail_3 = [{"gender":"male"}, {"score1":47},{"score2":83}]


print("이름 : %s, 학번 : %d, 학년 : %d, 학생정보 : %s" %(student_name_1,student_number_1,student_grade_1,student_detail_1))
print("이름 : {}, 학번 : {:3d}, 학년 : {:4d}, 학생정보 : {}".format(student_name_1,student_number_1,student_grade_1,student_detail_1))


