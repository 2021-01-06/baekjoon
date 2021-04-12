# 별 찍기

n = int(input())

for i in range(2*n):
    for j in range(n):
        if not (i+j) % 2:
            print('*', end='')
        else:
            print(' ', end='')
    print()