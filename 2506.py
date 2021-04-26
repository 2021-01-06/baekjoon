# 가산점 문제

n = int(input())

qs = list(map(int, input().split()))

r = 0
acc = 0
for i in range(len(qs)):
    if qs[i] == 0:
       acc = 0
       r += 0
    else:
        acc += 1
        r += acc

print(r)