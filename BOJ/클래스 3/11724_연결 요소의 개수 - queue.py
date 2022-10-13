# silver 2
# 816ms

import sys


def bfs(root):
    que = [root]
    visited[root] = 1

    while que:
        v = que.pop(0)

        for w in graph[v]:
            if not visited[w]:
                visited[w] = 1
                que.append(w)


N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0

for i in range(1, N+1):
    if not visited[i]:
        bfs(i)
        cnt += 1

print(cnt)
