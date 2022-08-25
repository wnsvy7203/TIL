def bfs(G, v, n):
    visited = [0] * (n+1)
    queue = [v]
    visited[v] = 1
    while queue:
        t = queue.pop(0)
        visited(t)
        for i in G[t]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[t] + 1
