# 배추를 지키자
# bfs로 이어져 있는 배추들을 방문하면서 0으로 만들어 준다
# 결과는 지렁이 갯수만 출력
# bfs를 이용하기 위한 deque import
from collections import deque

# 함수 bfs를 만들장 (m, n)을 받아버려
def bfs(n, m):
    queue = deque()
    # 시작점 넣기
    queue.append((n, m))
    v[n][m] = 0
    # 동서남북을 확인한후 방문안한 노드이면 그 노드를 추가
    while queue:
        n, m = queue.popleft()
        for d in range(4):
            x, y = m + dx[d], n + dy[d]
            if 0 <= x < M and 0 <= y < N:
                if v[y][x] == 1:
                    v[y][x] = 0
                    queue.append((y, x))

# get input()
# 테스트 갯수
T = int(input())
# 차례대로 배추밭의 가로 세로 갯수
# 동서 남북을 표현할 튜플 선언
dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

# 배추 지렁이? 의 수


for _ in range(T):
    M, N, K = map(int, input().split())
    # 배추를 저장할 집합과 배추의 위치들을 입력받는다
    v = [[0 for i in range(M)] for j in range(N)]
    for i in range(K):
        m, n = map(int, input().split())
        v[n][m] = 1
    c = 0
    for i in range(M):
        for j in range(N):
            if v[j][i] == 1:
                bfs(j, i)
                c += 1
    print(c)
