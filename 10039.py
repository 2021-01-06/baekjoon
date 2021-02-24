# 5명의 점수를 받아 평균을 출력한다
# 40점 이하는 40점으로 처리
mean=0
for i in range(5):
    grade=int(input())
    if grade>=40:
        pass
    else:
        grade=40
    mean+=int(grade/5)
print(mean)
