# silver 2
# 788ms

import sys
sys.setrecursionlimit(60000000)


def connected(x):
    visited[x] = 1

    for y in graph[x]:
        if not visited[y]:
            visited[y] = 1
            connected(y)


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
        connected(i)
        cnt += 1

print(cnt)
