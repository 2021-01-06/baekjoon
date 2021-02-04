import sys, copy

N, M = map(int, sys.stdin.readline().split())
ar=[]
def promising(a, n):
    if len(a)==0 or a[-1]<=n:
        return True
    else:
        return False
def dfs(a):
    if len(a)==M:
        ar.append(copy.deepcopy(a))
        return
    for i in range(1, N+1):
        if promising(a, i):
            a.append(i)
            dfs(a)
            a.pop()
dfs([])
for a in ar:
    print(*a)