# gold 5
# 0ms

import sys
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(y, x):
    day = 0
    que = deque([(y, x)])

    while que:
        day += 1

        for _ in range(len(que)):
            r, c = que.popleft()
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]

                if nr < 0 or nc < 0 or nr >= N or nc >= M:
                    continue

                if tomato[nr][nc] == 0:
                    tomato[nr][nc] = tomato[r][c] + 1
                    visited[nr][nc] = 1
                    que.append((nr, nc))

    for k in range(N):
        if 0 in tomato[k]:
            return -1
    else:
        return day-1


M, N = map(int, sys.stdin.readline().split())
tomato = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

res = 0
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1 and not visited[i][j]:
            res = bfs(i, j)
            break

print(res)
