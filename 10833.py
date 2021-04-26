# 대구사람이다

n = int(input())
remained = 0
for _ in range(n):
    stu_num, app_num = map(int, input().split())
    remained += app_num % stu_num
print(remained)