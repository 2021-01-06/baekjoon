# 웜 바이러스위 위험성
# 웜 바이러스는 이어진 간선으로 이어진 컴퓨터를 모두 감염
# 이어인 그래프를 순회하면 끝

# dfs or bfs 를 이용하여 순회


# 그래프를 입력 받자
# 이번에는 딕셔너리를 이용해보장

# 컴퓨터의 수
n = int(input())

# 간선의 수
e = int(input())

graphs = dict()
# 간선들
for _ in range(e):
    start, end = map(int, input().split())

    # 없으면 리스트를 만들어서 넣고 있으면 리스트에 어펜드
    # 쌍방향이므로 반대로도 수행
    if start not in graphs.keys():
        graphs[start] = [end]
    else:
        graphs[start].append(end)

    if end not in graphs.keys():
        graphs[end] = [start]
    else:
        graphs[end].append(start)
#
# # 그래프가 잘들어 갔는지 확인 출력
# print(graphs)

# 바이러스는 만연하게 퍼지니깐 bfs로 접근하는게 더 합당

# n번 컴퓨터가 감염 됬는지 안됬는지 확인
visited = [0] * (n + 1)

from collections import deque
# 감염된 컴퓨터수는 vistied의 합
def bfs(v):
    # 1번 컴퓨터에 관련된 바이러스 수를 출력 하는거넴
    visited[v] = 1
    queue = deque([])
    for _ in graphs[v]:
        queue.append(_)

    while queue:
        v = queue.popleft()
        # 이어진 간선에 대해
        # 방문안한 노드이면 큐에 추가
        for _ in graphs[v]:
            if visited[_] == 0:
                visited[_] = 1
                for i in graphs[_]:
                    queue.append(i)

bfs(1)
print(sum(visited)-1)