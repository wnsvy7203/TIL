# gold 5
# 2808ms

import sys
from collections import deque

dh = [-1, 1]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs():
    while que:
        h, r, c = que.popleft()

        visited[h][r][c] = 1

        for dy in range(2):
            nh = h + dh[dy]

            if nh < 0 or nh >= H:
                continue

            if tomatoes[nh][r][c] == 0:
                tomatoes[nh][r][c] = tomatoes[h][r][c] + 1
                visited[nh][r][c] = 1
                que.append((nh, r, c))

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if nr < 0 or nc < 0 or nr >= N or nc >= M:
                continue

            if tomatoes[h][nr][nc] == 0:
                tomatoes[h][nr][nc] = tomatoes[h][r][c] + 1
                visited[h][nr][nc] = 1
                que.append((h, nr, nc))


M, N, H = map(int, sys.stdin.readline().split())

tomatoes = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]

que = deque()
visited = [[[0] * M for _ in range(N)] for _ in range(H)]
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomatoes[i][j][k] == 1 and not visited[i][j][k]:
                que.append((i, j, k))
                visited[i][j][k] = 1

bfs()

res = 0
for tomato in tomatoes:
    for i in tomato:
        for j in i:
            if j == 0:
                print(-1)
                exit(0)
        else:
            res = max(res, max(i))
print(res-1)
