# ;;
from itertools import combinations
t = [n*(n+1)//2 for n in range(1, 45)]
e = [0] * 1001
for i in t:
    for j in t:
        for k in t:
            if i + j + k <= 1000:
                e[i + j + k] = 1
test_num = int(input())
for _ in range(test_num):
    print(e[int(input())])
