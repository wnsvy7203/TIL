# gold 4
# 724ms

import sys
import heapq


def dijkstra(s):
    visited[s] = 0
    heapq.heappush(heap, (0, s))

    while heap:
        tmp, value = heapq.heappop(heap)

        if visited[value] < tmp:
            continue

        for n, val in graph[value]:
            cost = val + tmp

            if cost < visited[n]:
                visited[n] = cost
                heapq.heappush(heap, (cost, n))


V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
INF = float('inf')
N = V + 1
heap = []
graph = [[] for _ in range(N)]
visited = [INF] * N

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

dijkstra(K)

for i in range(1, N):
    if visited[i] == INF:
        print('INF')
    else:
        print(visited[i])
