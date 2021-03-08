# 아주 중요한 문제
# 치킨 거리의 최소한으로 만들어라
from itertools import combinations
n, m = map(int, input().split())

# 0, 1, 2 빈칸, 집, 치킨
s = []
for i in range(n):
    s.append(list(map(int, input().split())))

def d(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

sc = []
sh = []
for i in range(n):
    for j in range(n):
        if s[i][j] == 1:
            sh.append((i, j))
        if s[i][j] == 2:
            sc.append((i, j))
c = combinations(sc, m)
r = float('inf')
for i in c:
    mr = 0
    for j in sh:
        mn = 100
        for k in i:
            mn = min(mn, d(j, k))
        mr += mn
    r = min(mr, r)
print(r)