# silver 1
# 68ms

import sys

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def find(r, c):
    global visit
    visited[r][c] = 1
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]

        if 0 <= nr < N and 0 <= nc < N and graph[nr][nc] and not visited[nr][nc]:
            find(nr, nc)
            visit += 1

    return visit


N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

cnt = []
for i in range(N):
    for j in range(N):
        if graph[i][j] and not visited[i][j]:
            visit = 1
            cnt.append(find(i, j))

cnt.sort()

print(len(cnt))
for i in cnt:
    print(i)
