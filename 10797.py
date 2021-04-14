# 쉽네
n = int(input())
n_li = map(int, input().split())
s = 0
for i in n_li:
    if i == n:
        s+=1
print(s)