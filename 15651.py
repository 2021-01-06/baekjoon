import sys, copy

N, M = map(int, sys.stdin.readline().split())
answers=[]
visited = [False]*N
def promising(array, n):
    return True

def dfs(arr, N, M):
    if len(arr)==M:
        print(*arr)
        return
    for i in range(N):
        if promising(arr, i+1):
            visited[i] = True
            arr.append(i+1)
            dfs(arr, N, M)
            visited[i] = False
            arr.pop()
dfs([], N, M)
