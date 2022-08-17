def dfs(v):
    print(v)
    top = 0

    visited[v] = 1      # 시작점 방문 표시
    while True:
        for w in adjList[v]: # v의 인접 정점 중 방문 안 한 정점 w가 있으면
            if visited[w] == 0:
                top += 1     # push(v)
                stack[top] = v
                v = w        # w 방문
                print(v)     # 방문 확인
                visited[w] = 1
                break
        else:                # w가 없으면
            if top != 0:
                v = stack[top]
                top -= 1
            else:
                break

V, E = map(int, input().split())
N = V + 1
adjList = [[] for _ in range(N)]
a, b = [map(int, input().split()) for _ in range(N)]
adjList[a].append(b)
adjList[b].append(a)

visited = [0] * N
stack = [0] * N

dfs(1)