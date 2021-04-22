# 규칙 유추


n = int(input())


for j in range(n-1, 0, -1):
    print(' '*j+'*'*(n-j))
print('*'*n)
for j in range(n-1, 0, -1):
    print(' '*(n-j)+'*'*j)
