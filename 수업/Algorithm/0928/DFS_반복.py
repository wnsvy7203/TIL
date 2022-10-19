def dfs(root):
    stk = [root]
    while stk:
        v = stk.pop()
        if not visited[v]:
            visited[v] = 1
            print(v, end=' ')

        for w in graph[v]:
            if not visited[w]:
                stk.append(w)


arr = list(map(int, input().split()))
N = len(arr) // 2

graph = [[] for _ in range(N+1)]
for i in range(N):
    graph[arr[i*2]].append(arr[i*2 + 1])
    graph[arr[i*2 + 1]].append(arr[i*2])

visited = [0] * (N+1)
dfs(1)
