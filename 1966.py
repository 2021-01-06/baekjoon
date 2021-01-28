# 가장앞의 문서의 중요도를 확인

import sys
from collections import deque

test_num = int(sys.stdin.readline().strip())
for _ in range(test_num):
    n, m = map(int, sys.stdin.readline().split())
    pr_li = deque(map(int, sys.stdin.readline().split()))
    q = deque([0 for x in range(n)])
    q[m] = 1
    cnt = 0
    # pr_li : 중요도 리스트 q : 자료 리스트
    while True:
        if pr_li[0]==max(pr_li):
            cnt+=1
            if q[0]==1:
                print(cnt)
                break
            else:
                pr_li.popleft()
                q.popleft()
        else:
            pr_li.append(pr_li[0])
            pr_li.popleft()
            q.append(q[0])
            q.popleft()