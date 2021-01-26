import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
circle = deque([x for x in range(1, n+1)])

answer_sheet = []
while circle:
    for x in range(k-1):
        circle.append(circle.popleft())
    answer_sheet.append(circle.popleft())

print('<'+', '.join(map(str, answer_sheet))+'>')
