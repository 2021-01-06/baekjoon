# # 정수 Queue 구현
# # list로
#
# def q_push(l, x):
#     l.append(x)
#
# def q_pop(l):
#     if len(l) == 0:
#         print(-1)
#     else:
#         print(l.pop(0))
#
# def q_size(l):
#     print(len(l))
#
# def q_empty(l):
#     if len(l) == 0:
#         print(1)
#     else:
#         print(0)
#
# def q_front(l):
#     if len(l) == 0:
#         print(-1)
#     else:
#         print(l[0])
#
# def q_back(l):
#     if len(l) == 0:
#         print(-1)
#     else:
#         print(l[-1])
#
# queue = list()
#
# n = int(input())
# for i in range(n):
#     o1 = input()
#     o1 = o1.split()
#     try:
#         o2 = int(o1[1])
#     except:
#         pass
#     o1 = o1[0]
#     if o1 == 'push':
#         q_push(queue, o2)
#     elif o1 == 'front':
#         q_front(queue)
#     elif o1 == 'back':
#         q_back(queue)
#     elif o1 == 'size':
#         q_size(queue)
#     elif o1 == 'pop':
#         q_pop(queue)
#     elif o1 == 'empty':
#         q_empty(queue)
#

# 시간초과 실화냐
# 라이브러리 써야지
from collections import deque
q =deque()

n = int(input())

for i in range(n):
    o = input()
    o = o.split()
    try:
        x = o[1]
    except:
        pass
    o = o[0]
    if o == 'push':
        q.append(x)
    elif o == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif o == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif o == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])
    elif o == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(-1)
    elif o == 'size':
        print(len(q))
