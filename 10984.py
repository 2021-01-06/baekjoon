grade_num = int(input())
for _ in range(grade_num):
    num = int(input())
    total_n = 0
    ga = 0
    for i in range(num):
        n, g = map(float, input().split())
        total_n += n
        ga += n*g
    print(int(total_n), round(ga/total_n, 1))