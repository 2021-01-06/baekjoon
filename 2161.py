# 회전 큐 같당?

from collections import deque

max_num = int(input())

my_list = [i for i in range(1, max_num+1)]
my_q = deque(my_list)
my_result = []
while my_q:
    my_result.append(my_q.popleft())
    # predict 2
    my_q.rotate(-1)

print(*my_result)
