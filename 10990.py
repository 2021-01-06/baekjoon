# 별을 찍장
n = int(input())

for i in range(n):
    f = ' ' * (n-i-1)
    b = ' ' * (2*i-1)
    if i == 0:
        print(f, '*', sep='')
    else:
        print(f, '*', b, '*', sep='')
