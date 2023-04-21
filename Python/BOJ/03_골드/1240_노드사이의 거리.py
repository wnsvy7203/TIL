# gold 5
# 304ms

import sys
from collections import deque


def distance(a, b):
    visited = [-1 for _ in range(N+1)]
    visited[a] = 0

    queue = deque([a])

    while queue:
        n = queue.popleft()
        for g, d in graph[n]:
            if visited[g] == -1:
                visited[g] = visited[n] + d
                queue.append(g)

            if g == b:
                return visited[g]


N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    print(distance(s, e))
