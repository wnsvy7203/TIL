"""
bfs
"DFS와 방문체크 시점이 다름"
- 이미 방문한 곳을 다시 Queue에 넣는 중복 과정을 제거하기 위함!
"""
import sys
from pprint import pprint

sys.stdin = open('input.txt')


def BFS(v):
    queue = [v]
    print(v, end=' ')
    # 방문표시 먼저 진행
    visited[v] = 1

    while queue:
        v = queue.pop(0)
        for w in range(1, V + 1):
            # 해당 정점(V)의 인접 정점(W)이면서,
            # 이 인접정점에 아직 방문하지 않았다면
            if G[v][w] == 1 and visited[w] == 0:
                # 인접 정점을 방문하기 위해 queue에 추가
                queue.append(w)
                visited[w] = 1
                print(w, end=' ')


# V(ertex), E(dge)
V, E = map(int, input().split())

# 간선 정보 초기화
temp = list(map(int, input().split()))
# pprint(temp)

# Graph 초기화
G = [[0] * (V + 1) for _ in range(V + 1)]
# pprint(G)

# 인접행렬 작성(간선 정보)
for i in range(E):
    n1, n2 = temp[i * 2], temp[i * 2 + 1]
    G[n1][n2] = 1
    G[n2][n1] = 1
# pprint(G)

# 방문 표시 초기화
visited = [0 for _ in range(V + 1)]
# pprint(visited)

# bfs 탐색 시작
BFS(1)