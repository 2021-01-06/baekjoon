import sys
#
# test_num = int(sys.stdin.readline().strip())
# li = list(map(int, sys.stdin.readline().split()))
#
# result = []
# for idx, value in enumerate(li):
#     stk = li.copy()
#     nge = value
#     for i in range(idx+1, len(li)):
#         temp_pop = stk.pop()
#         if temp_pop > value:
#             nge = temp_pop
#     if nge == value:
#         nge = -1
#
#     result.append(nge)
#
# sys.stdout.write(*result)
#

import sys

N = int(sys.stdin.readline().strip())

input = list(map(int, sys.stdin.readline().split()))
stack = []
result = [-1 for _ in range(N)]

stack.append(0)
i = 1
while stack and i < N:
    while stack and input[stack[-1]] < input[i]:
        result[stack[-1]] = input[i]
        stack.pop()

    stack.append(i)
    i += 1

print(*result)