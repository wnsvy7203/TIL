# gold 4
# pypy 로만 통과 = 5056ms

import sys

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(r, c, v):
    global cnt

    visited[ord(board[r][c]) - 65] = 1
    cnt = max(cnt, v)
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]

        if 0 <= nr < R and 0 <= nc < C:
            if not visited[ord(board[nr][nc]) - 65]:
                dfs(nr, nc, v+1)
                visited[ord(board[nr][nc]) - 65] = 0


R, C = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(R)]

visited = [0 for _ in range(26)]
cnt = 0
dfs(0, 0, 1)

print(cnt)
