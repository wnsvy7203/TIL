# silver 1
# 108ms

import sys
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs():
    que = deque([(0, 0)])

    while que:
        r, c = que.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and miro[nr][nc]:
                que.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1


N, M = map(int, sys.stdin.readline().split())
miro = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
visited[0][0] = 1

bfs()

print(visited[N-1][M-1])
