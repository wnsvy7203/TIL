def bfs(v, n):
    visited = [0] * (n+1)
    queue = [v]
    visited[v] = 1
    while queue:
        v = queue.pop(0)
        print(v)
        for w in adjList[v]:
            if visited[w] == 0:
                queue.append(w)
                visited[w] = visited[v] + 1


V, E = map(int, input().split())
N = V + 1
adjList = [[] for _ in range(N)]
arr = list(map(int, input().split()))
for i in range(0, 2*E, 2):
    adjList[arr[i]].append(arr[i+1])
    adjList[arr[i+1]].append(arr[i])

bfs(1, 7)