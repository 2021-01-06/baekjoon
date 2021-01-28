import sys
from collections import deque

cards = list(range(1, int(sys.stdin.readline().strip())+1))
q = deque(cards)
while len(q) > 1:

    q.popleft()
    q.append(q.popleft())

print(*q)