# 별찍기 놀이
n = int(input())
for i in range(n):
    f = ' ' * (n-i-1)
    s = '*' *(2*i + 1)
    print(f, s, sep='')
for i in range(n-2, -1, -1):
    f = ' ' * (n-i-1)
    s = '*' *(2*i + 1)
    print(f, s, sep='')