# DFS BFS 출력하는 프로그램을 작성하시오
# 방문할게 많을 때 정점 번호가 작은 것 부터 방문... -> 리스트 이용
# 번호는 1~N 리스트

# N 정점의 갯수, M 간선의 갯수, v 시작노드의 번호
N, M, v = map(int, input().split())

# 입력을 받기 위한 리스트 s[1][2]=1 means node 1 - node 2 is connected
# s는 node만큼 생겨야 겠죵 0 인덱스는 무시하입시다.
s=[[0] * (N + 1) for _ in range(N + 1)]

# 모서리들을 연결하기
for _ in range(M):
    start, end = map(int, input().split())
    s[start][end] = 1
    s[end][start] = 1

# dfs
# dfs -> 깊이 우선 탐탐색 첫 노드 방문 그다음 노드 방문 방문 방문 방문
# 재귀적으로 가능할 듯?
# 노드 v에 방문한다.

# 함수 안에서 뺴왔음

def dfs(v):
    # 노드 v에 방문한다.
    # 방문 한다 -> print()
    print(v, end=' ')
    # we need to check if this node is visted or not
    # we need to declare visited list
    # v 노드는 방문했다
    visited[v] = 1

    # 각각의 노드를 방문한다.
    for _ in range(1, N + 1):
        # 방문한 노드가 아니고 간선이 이어져 있으면 깊이를 쌓아간다
        if visited[_] == 0 and s[v][_] == 1:
            dfs(_)

# bfs
# bfs 는 전형적으로 deque로 구현하징
# deque 넣고 하나씩 왼쪽부터 뽑으면서 없어질때까지 방문하기

from collections import deque
def bfs(v):
    # 시작점 추가
    start = deque([v])
    # 방문 초기화
    for _ in range(1, N+1):
        visited[_] = 0
    # 방문할 것이 없어질 때까지 방문하기
    visited[v]=1

    while start:
        v = start.popleft()
        print(v, end=' ')

        # 방문할수 있는것 다 추가하기
        for _ in range(1, N + 1):
            if visited[_] == 0 and s[v][_] == 1:
                start.append(_)
                visited[_] = 1

visited=[0] * (N + 1)
dfs(v)
print()
bfs(v)
