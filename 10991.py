# 별 출력

n = int(input())

for i in range(n):
    f = ' ' * (n-i-1)
    s = f + '*'
    if i >= 1:
        s += ' *' * i
    print(s)