# 별찍기 놀이

n = int(input())
for i in range(n):
    s = '*' * (i+1)
    b = ' ' * 2*(n-i-1)
    print(s, b, s, sep='')
for i in range(n-2, -1, -1):
    s = '*' * (i + 1)
    b = ' ' * 2 * (n - i - 1)
    print(s, b, s, sep='')