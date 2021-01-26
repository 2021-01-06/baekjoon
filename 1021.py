import sys
from collections import deque
n, m = map(int,sys.stdin.readline().split())
num_li=list(map(int,sys.stdin.readline().split()))
q = deque([x for x in range(1, n+1)])
cnt=0
for num in num_li:
    idx = q.index(num)
    if idx<len(q)-idx:
        while True:
            if q[0]==num:
                q.popleft()
                break
            else:
                q.append(q[0])
                q.popleft()
                cnt+=1
    else:
        while True:
            if q[0]==num:
                q.popleft()
                break
            else:
                q.appendleft(q[-1])
                q.pop()
                cnt+=1
print(cnt)