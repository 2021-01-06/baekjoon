# 순환큐를 구현하고싶은데 아니넹
from collections import deque

n, k = map(int, input().split())
temp = []
for i in range(1, n+1):
    temp.append(i)

my_q = deque(temp)

result_list = []
r = 0
while my_q:
    r += 1
    if r == k:
        r = 0
        result_list.append(str(my_q.popleft()))
    else:
        my_q.append(my_q.popleft())

text = ', '.join(result_list)
print('<', text, '>', sep='')