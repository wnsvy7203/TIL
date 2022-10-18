import sys
from collections import deque


def bfs(root):
    visited = [0] * (N+1)
    queue = deque([root])
    visited[root] = 1

    while queue:
        p = queue.popleft()
        for q in graph[p]:
            if not visited[q]:
                queue.append(q)
                visited[q] = visited[p] + 1

    return sum(visited) - N


N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    v, w = map(int, sys.stdin.readline().split())

    graph[v].append(w)
    graph[w].append(v)

step = []

for i in range(1, N+1):
    step.append(bfs(i))

print(step.index(min(step)) + 1)
