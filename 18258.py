# import sys
#
# my_queue = []
#
# def push(queue, x):
#     queue.append(x)
#
# def pop(queue):
#     if queue:
#         print(queue.pop(0))
#     else:
#         print(-1)
#
# def size(queue):
#     print(len(queue))
#
# def empty(queue):
#     if len(queue) == 0:
#         print(1)
#     else:
#         print(0)
#
# def front(queue):
#     if len(queue) > 0:
#         print(queue[0])
#     else:
#         print(-1)
#
# def back(queue):
#     if len(queue) > 0:
#         print(queue[-1])
#     else:
#         print(-1)
#
# test_num = int(sys.stdin.readline().strip())
# for n in range(test_num):
#     order = sys.stdin.readline().split()
#     if order[0] == 'push':
#         push(my_queue, int(order[1]))
#     elif order[0] == 'front':
#         front(my_queue)
#     elif order[0] == 'back':
#         back(my_queue)
#     elif order[0] == 'size':
#         size(my_queue)
#     elif order[0] == 'empty':
#         empty(my_queue)
#     elif order[0] == 'pop':
#         pop(my_queue)


import sys
from collections import deque

my_queue = deque()

def push(queue, x):
    queue.append(x)

def pop(queue):
    if queue:
        print(queue.popleft())
    else:
        print(-1)

def size(queue):
    print(len(queue))

def empty(queue):
    if len(queue) == 0:
        print(1)
    else:
        print(0)

def front(queue):
    if len(queue) > 0:
        print(queue[0])
    else:
        print(-1)

def back(queue):
    if len(queue) > 0:
        print(queue[-1])
    else:
        print(-1)

test_num = int(sys.stdin.readline().strip())
for n in range(test_num):
    order = sys.stdin.readline().split()
    if order[0] == 'push':
        push(my_queue, int(order[1]))
    elif order[0] == 'front':
        front(my_queue)
    elif order[0] == 'back':
        back(my_queue)
    elif order[0] == 'size':
        size(my_queue)
    elif order[0] == 'empty':
        empty(my_queue)
    elif order[0] == 'pop':
        pop(my_queue)
