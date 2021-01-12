import sys
n = int(input())
for i in range(n):
    cnt = 0
    li = list(map(int, sys.stdin.readline().split()))
    for n in li[1:]:
        if n > sum(li[1:])/li[0]:
            cnt += 1
    print('%.3f' % round((cnt / li[0] * 100), 3)+"%")
