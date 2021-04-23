# 집합구현

n = int(input())

for _ in range(n):
    order = input().split()
    o = order[0]
    try:
        s = order[1]
    except IndexError:
        pass
