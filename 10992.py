# 별 찍기
n = int(input())

for i in range(n):
    f = ' ' * (n-i-1)
    b = ' ' * (2*i-1)
    if i == 0:
        print(f, '*', sep='')
    elif i == n-1:
        print('*'* (2*n-1))
    else:
        print(f, '*', b, '*', sep='')
