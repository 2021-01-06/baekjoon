# 단순한 미로문제
# ! 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다
from collections import deque
# 입력
N, M = map(int, input().split())
s = []
for i in range(N):
    s.append(list(input()))

# 각종 변수들 선언
# 동서남북, 칸수
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
c = 0
cs = []
# bfs 구현

def bfs(n, m):
    global c
    queue = deque()
    queue.append([n, m])
    s[n][m] = 1
    while queue:
        x, y = queue.popleft()
        for _ in range(4):
            nx = dx[_] + x
            ny = dy[_] + y
            if 0 <= nx < N and 0 <= ny < M and s[nx][ny] == '1':
                    queue.append([nx, ny])
                    s[nx][ny] = s[x][y] + 1

bfs(0, 0)
print(s[N-1][M-1])

# 출력