# 딕션너리 쓰면 될듯
from collections import defaultdict
n ,m = map(int, input().split())
my_dict = dict()
for i in range(n):
    s = input().strip()
    my_dict.setdefault(s, 0)

for i in range(m):
    s = input().strip()
    if s in my_dict:
        my_dict[s] += 1

print(sum(my_dict.values()))