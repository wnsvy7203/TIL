# gold 3
# 180ms

# 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때,
# 지나야하는 칸의 개수의 최솟값이다.
# 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기,
# 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.

import sys
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(y, x, size):
    # 아기 상어로부터의 거리를 담을 리스트 dist
    dist = [[0] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    que = deque([(y, x)])
    visited[y][x] = 1
    lst = []

    while que:
        r, c = que.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                if graph[nr][nc] <= size:
                    que.append((nr, nc))
                    visited[nr][nc] = 1
                    dist[nr][nc] = dist[r][c] + 1
                    if graph[nr][nc] < size and graph[nr][nc]:
                        lst.append((nr, nc, dist[nr][nc]))

    # 거리를 매개로 정렬한다.
    # 뒤에서부터 pop 할 거니까 거리에 제일 가까운 게 맨 뒤로 가야 한다.
    # 거리가 같다면 왼쪽 위에서부터 출발하게끔 해야 한다.
    # y가 작은 놈이 먼저 나와야 하고, y가 같다면 x가 작은 놈이 먼저 나와야 한다.
    lst.sort(key=lambda z: (-z[2], -z[0], -z[1]))
    return lst


N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
temp = []
a, b, shark = 0, 0, 2

for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            a, b = i, j

cnt = 0
res = 0
while True:
    temp = bfs(a, b, shark)

    if not temp:
        break

    # far 은 좌표 (a, b) -> (na, nb)로 가는 거리
    na, nb, far = temp.pop()

    res += far
    graph[a][b] = 0
    graph[na][nb] = 0

    a, b = na, nb
    cnt += 1
    if cnt == shark:
        shark += 1
        cnt = 0

print(res)
