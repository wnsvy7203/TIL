# silver 2
# 80ms
# RecursionError 가 나기 때문에 횟수만 늘려주면 가볍게 통과

import sys
sys.setrecursionlimit(20000000)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def find(r, c):
    visited[r][c] = 1
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]

        if 0 <= nr < N and 0 <= nc < M and graph[nr][nc] and not visited[nr][nc]:
            find(nr, nc)


T = int(sys.stdin.readline())

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    graph = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        graph[Y][X] = 1

    cnt = 0

    for i in range(N):
        for j in range(M):
            if graph[i][j] and not visited[i][j]:
                cnt += 1
                find(i, j)

    print(cnt)
