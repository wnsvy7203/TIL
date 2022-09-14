def bfs(v, N, t):               # v: 시작 정점, N: 마지막 정점 번호, t: 찾는 정점
    visited = [0] * (N + 1)      # visited 생성
    q = []                      # 큐 생성
    q.append(v)                 # 시작점 인큐
    visited[v] = 1              # 시작점 방문 표시

    while q:                    # 큐가 비어있지 않으면
        v = q.pop(0)            # 디큐
        if v == t:              # visit(v)
            return 1  # 목표 발견
        for w in adjList[v]:    # v에 인접하고 방문 안 한 w 인큐, 표시
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[v] + 1
    return 0


T = 10
for _ in range(T):
    tc, E = map(int, input().split())
    arr = list(map(int, input().split()))

    adjList = [[] for _ in range(100)]
    for i in range(E):
        a, b = arr[i*2], arr[i*2+1]
        adjList[a].append(b)

    print(adjList)
