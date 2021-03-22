# 으 머리아파
from itertools import combinations

l, c = map(int, input().split())
s = list(input().split())
s.sort()

# 걍 이터툴로 조합을 만듬 친절하게 앞에서부터 만들어주네
com = combinations(s, l)
for i in com:
    v, w = 0, 0
    for j in i:
        if j in 'aieou':
            v += 1
        else:
            w += 1
    if v >= 1 and w >= 2:
        print(''.join(i))