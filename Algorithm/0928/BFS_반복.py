def bfs(root):
    que = [root]
    while que:
        v = que.pop(0)
        if not visited[v]:
            visited[v] = 1
            print(v, end=' ')

        for w in graph[v]:
            if not visited[w]:
                que.append(w)


arr = list(map(int, input().split()))
N = len(arr) // 2

graph = [[] for _ in range(N+1)]
for i in range(N):
    graph[arr[i*2]].append(arr[i*2 + 1])
    graph[arr[i*2 + 1]].append(arr[i*2])

visited = [0] * (N+1)
bfs(1)
