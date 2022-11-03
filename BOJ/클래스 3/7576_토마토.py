# gold 5
# 2056ms

import sys
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs():
    while que:
        r, c = que.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if nr < 0 or nc < 0 or nr >= N or nc >= M:
                continue

            if tomato[nr][nc] == 0:
                tomato[nr][nc] = tomato[r][c] + 1
                que.append((nr, nc))


M, N = map(int, sys.stdin.readline().split())
tomato = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
que = deque()

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1 and not visited[i][j]:
            que.append((i, j))
            visited[i][j] = 1

bfs()

res = 0
for i in tomato:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    else:
        res = max(res, max(i))
print(res-1)
