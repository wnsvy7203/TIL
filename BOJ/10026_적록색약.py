# gold 5
#

import sys
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def color(y, x):
    saved = grid[y][x]
    que = deque([(y, x)])

    while que:
        r, c = que.popleft()
        visited1[r][c] = 1

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < N and 0 <= nc < N:
                if grid[nr][nc] == saved and not visited1[nr][nc]:
                    que.append((nr, nc))


def color_weak(y, x):
    if grid[y][x] == 'R' or grid[y][x] == 'G':
        saved = ('R', 'G')
    else:
        saved = grid[y][x]

    que = deque([(y, x)])

    while que:
        r, c = que.popleft()
        visited2[r][c] = 1

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < N and 0 <= nc < N and not visited2[nr][nc]:
                if type(saved) == str and grid[nr][nc] == saved:
                    que.append((nr, nc))
                elif type(saved) == tuple and grid[nr][nc] in saved:
                    que.append((nr, nc))


N = int(sys.stdin.readline())

grid = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
visited1 = [[0 for _ in range(N)] for _ in range(N)]
visited2 = [[0 for _ in range(N)] for _ in range(N)]

cnt1 = 0
cnt2 = 0

for i in range(N):
    for j in range(N):
        if not visited1[i][j]:
            color(i, j)
            cnt1 += 1

        if not visited2[i][j]:
            color_weak(i, j)
            cnt2 += 1

print(cnt1, cnt2)
