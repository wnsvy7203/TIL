import sys


def dfs(r, c):
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    visited = [[0] * 5 for _ in range(5)]
    visited[r][c] = 1
    stk = [[-1, -1] * 5 for _ in range(5)]
    stk[r][c] = [r, c]
    cnt = 1
    while cnt <= 6:
        for r in range(5):
            for c in range(5):
                for k in range(4):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    if 0 > nr or nr >= 5 or 0 > nc or nc >= 5:
                        continue

                    if visited[nr][nc] == 0:
                        cnt += 1
                        visited[nr][nc] = 1





digit = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]
