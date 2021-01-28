from collections import deque
import sys

test_num = int(sys.stdin.readline().strip())
q = deque([])
for _ in range(test_num):
    order = sys.stdin.readline().split() # n은 문자열
    if order[0]=='push_back':
        q.append(int(order[1]))
    elif order[0]=='push_front':
        q.appendleft(int(order[1]))
    elif order[0]=='front':
        if len(q)!= 0:
            print(q[0])
        else:
            print(-1)
    elif order[0]=='back':
        if len(q)!= 0:
            print(q[-1])
        else:
            print(-1)
    elif order[0]=='size':
        print(len(q))
    elif order[0]=='empty':
        if len(q):
            print(0)
        else:
            print(1)
    elif order[0]=='pop_front':
        if len(q)!=0:
            print(q.popleft())
        else:
            print(-1)
    elif order[0]=='pop_back':
        if len(q)!=0:
            print(q.pop())
        else:
            print(-1)

