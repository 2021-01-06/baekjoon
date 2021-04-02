from itertools import permutations
import sys
n = int(sys.stdin.readline())
# 참고
def dfs(i, s):
    global a
    if i == n:
        return

    a.add(s+l[i])
    dfs(i+1, s + l[i])
    dfs(i+1, s)

l = list(map(int, sys.stdin.readline().split()))
a = set(l[:])
dfs(0, 0)

for i in range(1, max(a)+2):
    if i not in a:
        print(i)
        break

# 시간..