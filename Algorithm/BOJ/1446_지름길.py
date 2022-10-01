# silver 1
# 0ms

import sys
import heapq


def dijkstra(x):
    visited[x] = 0
    heapq.heappush(heap, )


N, D = map(int, sys.stdin.readline().split())
heap = []
visited = []
graph = [0 for _ in range(D)]

for _ in range(N):
    u, v, w = map(int, sys.stdin.readline().split())
    if v < D and v - u > w:
        graph


dijkstra(0)

print()
