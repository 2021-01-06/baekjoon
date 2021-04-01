# 1 2 2 3 3 3 4 4 4 5 5 5 5
s, e = map(int, input().split())

n = []
for i in range(1, 46):
    n += [i] * i
print(sum(n[s-1:e]))