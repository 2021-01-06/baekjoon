# 같은 팀이 될때 까지 올라간다
# 같은 팀인지 구분 -> //2

N, a, b = map(int, input().split())

# 인덱스화
a -= 1
b -= 1

c = 0
while N:
    a //= 2
    b //= 2
    c += 1
    # 같은 팀이면
    if a == b:
        print(c)
        break
else:
    print(-1)

