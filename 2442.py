# 별찍기 놀이

n = int(input())

for i in range(n-1, -1, -1):
    f= ' '*i
    print(f + '*' * (2*n - 2*i -1))
