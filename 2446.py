# 별찍기

N = int(input())
M = 2 * N - 1

for i in range(N):
    f = ' ' * i
    s = '*' + '*' * (M-1-2*i)
    print(f + s)
for i in range(N-2, -1, -1):
    f = ' ' * i
    s = '*' + '*' * (M - 1 - 2 * i)
    print(f + s)