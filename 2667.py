# 단지번호 붙이기
# 2차원 배열을 그래프 탐색하기
n = int(input())

# 배열을 입력받장
m = []
for _ in range(n):
    m.append(list(map(int, input())))

# 1을 방문하고 만약 거기가 이어져있으면 계속 방문
# 동서남북
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 단지당 집을 저장할 리스트
h = []

from collections import deque

def bfs(i, j):
    # (i,j)를 받는 큐 생성
    queue = deque([(i, j)])
    # 방문 했음 = 0
    m[i][j] = 0
    # 집 세알리기 위한 변수
    c = 1
    while queue:
        x, y = queue.popleft()
        # 동서남북 학인
        for _ in range(4):
            nx, ny = x + dx[_], y + dy[_]
            # 경계 확인
            if (0 <= nx < n) and (0 <= ny < n):
                # 이어 졌으면 큐에추가 갯수 ++
                if m[nx][ny] == 1:
                    m[nx][ny] = 0
                    queue.append((nx, ny))
                    c += 1
    h.append(c)

for i in range(n):
    for j in range(n):
        # 1이면 한번 방문합시다
        if m[i][j] == 1:
            bfs(i, j)
print(len(h))
for i in sorted(h):
    print(i)
