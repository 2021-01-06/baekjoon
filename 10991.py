# 별 출력

n = int(input())

for i in range(n):
    for j in range(2*i+1):
        if (i+j)%2 :
            print(' ', end='')
        else:
            print('*', end='')
    print()