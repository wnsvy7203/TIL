# gold 5
# 120ms

# dfs 는 되는데 bfs 는 안 되는 이유는 뭐지?

import sys

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def color(y, x):
    global cnt1
    cnt1 += 1

    saved = grid[y][x]
    stk = [(y, x)]

    while stk:
        r, c = stk.pop()
        visited1[r][c] = 1

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < N and 0 <= nc < N:
                if grid[nr][nc] == saved and not visited1[nr][nc]:
                    stk.append((nr, nc))


def color_weak(y, x):
    global cnt2
    cnt2 += 1

    if grid[y][x] == 'R' or grid[y][x] == 'G':
        saved = ('R', 'G')
    else:
        saved = grid[y][x]

    stk = [(y, x)]

    while stk:
        r, c = stk.pop()
        visited2[r][c] = 1

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < N and 0 <= nc < N and not visited2[nr][nc]:
                if type(saved) == str and grid[nr][nc] == saved:
                    stk.append((nr, nc))
                elif type(saved) == tuple and grid[nr][nc] in saved:
                    stk.append((nr, nc))


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

        if not visited2[i][j]:
            color_weak(i, j)

print(cnt1, cnt2)
