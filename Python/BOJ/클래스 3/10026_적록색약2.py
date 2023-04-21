# gold 5
# 124ms

# dfs 는 되는데 bfs 는 안 되는 이유는 뭐지?

import sys

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def color(y, x):
    saved = grid[y][x]
    stk = [(y, x)]

    while stk:
        r, c = stk.pop()
        visited[r][c] = 1

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                if grid[nr][nc] == saved:
                    stk.append((nr, nc))


N = int(sys.stdin.readline())

grid = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]

cnt1 = 0
cnt2 = 0

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            color(i, j)
            cnt1 += 1

for i in range(N):
    for j in range(N):
        if grid[i][j] == 'R':
            grid[i][j] = 'G'

visited = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            color(i, j)
            cnt2 += 1

print(cnt1, cnt2)
