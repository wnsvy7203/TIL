# A ~ G - > 0 ~ 6
# adjList = [[1, 2],
#            [0, 3, 4],
#            [0, 4]
#            [1, 5]
#            [1, 2, 5]
#            [3, 4, 6]
#            [5]]

def bfs(v, N):                  # v: 시작 정점, N: 마지막 정점 번호
    visited = [0] * (N + 1)      # visited 생성
    q = []                      # 큐 생성
    q.append(v)                 # 시작점 인큐
    visited[v] = 1              # 시작점 방문 표시

    while q:                    # 큐가 비어있지 않으면
        v = q.pop(0)            # 디큐
        print(v)
        for w in adjList[v]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[v] + 1

V, E = map(int, input().split())
N = V + 1
adjList = [[] for _ in range(N)]
for _ in range(E):
    a, b = map(int, input().split())
    adjList[a].append(b)
    adjList[b].append(a)
bfs(0, V)