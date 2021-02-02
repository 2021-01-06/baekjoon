import sys, copy
N, M = map(int, sys.stdin.readline().split())
visited = [False]*N
answers=[]
def dfs(arr, N, M):
    if len(arr)==M:
        answers.append(copy.deepcopy(arr))
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            arr.append(i+1)
            dfs(arr, N, M)
            visited[i] = False
            arr.pop()
dfs([], N, M)

for answer in answers:
    print(*answer)