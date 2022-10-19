# D3
# 123ms

import heapq

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def dijkstra():
    visited[0][0] = 0
    heap = []
    heapq.heappush(heap, (0, 0, 0))

    while heap:
        tmp, r, c = heapq.heappop(heap)

        for d in range(4):
            nr = r + dy[d]
            nc = c + dx[d]

            if 0 <= nr < N and 0 <= nc < N:
                cnt = 1
                if fuel[nr][nc] > fuel[r][c]:
                    cnt += (fuel[nr][nc] - fuel[r][c])
                cost = tmp + cnt
                if cost < visited[nr][nc]:
                    visited[nr][nc] = cost
                    heapq.heappush(heap, (cost, nr, nc))


T = int(input())

for C in range(1, T+1):
    N = int(input())
    fuel = [list(map(int, input().split())) for _ in range(N)]
    visited = [[float('INF')] * N for _ in range(N)]
    dijkstra()

    print(f'#{C} {visited[-1][-1]}')
