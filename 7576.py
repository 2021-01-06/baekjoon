# 토마토
# 익은 토마토는 동서남북으로 전파
# 토마토가 없는 경우가 있음
# 최소 일수 혹은 불가능함을 출력


# 라이브러리
from collections import deque
# 입력

M, N = map(int, input().split())
s = [list(map(int, input().split())) for i in range(N)]

# 필요한 동서남북 변수
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# bfs로 토마토를 방문
def bfs():
    # 토마토 있는 곳 확인
    # 시작
    queue = deque()
    for i in range(N):
        for j in range(M):
            if s[i][j] == 1:
                queue.append([i, j])
    # 방문하면서 동서남북 이어져있으면 큐에 추가
    # 그리고 s를 날짜로 대체
    while queue:
        x, y = queue.popleft()
        for _ in range(4):
            nx, ny = x + dx[_], y + dy[_]
            if 0 <= nx < N and 0 <= ny < M and s[nx][ny] == 0:
                queue.append([nx, ny])
                s[nx][ny] = s[x][y] + 1

# 안 익은 토마토가 있는지 확인
bfs()

c = 0
m = -1
for i in s:
    for j in i:
        if j == 0:
            c = 1
        m = max(m, j)
    # 최소 일수를 프린트
if c:
    print(-1)
else:
    print(m - 1)