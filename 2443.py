# 별찍기

n = int(input())
for i in range(n):
    f = ' ' * i
    s = '*' * (2*(n-i-1)+1)
    print(f+s)
