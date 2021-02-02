import sys, copy

N, M = map(int, sys.stdin.readline().split())
answers=[]
visited = [False]*N
def promising(array, n):
    if len(array) == 0:
        return True
    if not visited[n-1] and n > array[-1]:
        return True
    else:
        return False
def dfs(arr, N, M):
    if len(arr)==M:
        answers.append(copy.deepcopy(arr))
        return
    for i in range(N):
        if promising(arr, i+1):
            visited[i] = True
            arr.append(i+1)
            dfs(arr, N, M)
            visited[i] = False
            arr.pop()
dfs([], N, M)
for answer in answers:
    print(*answer)