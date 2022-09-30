# silver 2
# 2552ms

import sys
import heapq


def dijkstra(x):
    visited[x] = 0
    heap = []
    heapq.heappush(heap, (0, x))

    while heap:
        tmp, v = heapq.heappop(heap)
        if visited[v] < tmp:
            continue
        for w in graph[v]:
            cost = tmp + 1
            if cost < visited[w]:
                visited[w] = cost
                heapq.heappush(heap, (cost, w))


N, M, K, X = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
visited = [1000000 for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

dijkstra(X)
res = []

for i in range(1, N+1):
    if visited[i] == K:
        res.append(i)

if res:
    for i in res:
        print(i)
else:
    print(-1)
