# 기차안에 사람들 세기
s = int(input().split()[1])
w = 0
for i in range(2):
    m, p = map(int, input().split())
    s -= m
    if m < 0:
        m = 0
    s += p
    if s > 10000:
        s = 10000
    if s > w :
        w = s
print(w)