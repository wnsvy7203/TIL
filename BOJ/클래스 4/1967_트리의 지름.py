# gold 4
# 112ms

import sys
from collections import deque


def bfs(x):
    visited = [-1 for _ in range(n + 1)]
    visited[x] = 0
    que = deque([x])

    while que:
        a = que.popleft()

        for b, d in graph[a]:
            if visited[b] == -1:
                que.append(b)
                visited[b] = visited[a] + d

    return visited.index(max(visited))


def bfs_find(x):
    visited = [-1 for _ in range(n + 1)]
    visited[x] = 0
    que = deque([x])

    while que:
        a = que.popleft()

        for b, d in graph[a]:
            if visited[b] == -1:
                que.append(b)
                visited[b] = visited[a] + d

    return max(visited)


n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

print(bfs_find((bfs(1))))


