# gold 5
# 64ms

import sys
from collections import deque


def bfs():
    que = deque([1])
    visited[1] = 1

    while que:
        temp = que.popleft()

        for i in range(1, 7):
            new = temp + i

            if 0 < new <= 100 and not visited[new]:
                cnt = graph[new]

                if not visited[cnt]:
                    que.append(cnt)
                    visited[cnt] = 1
                    step[cnt] = step[temp] + 1

                    if cnt == 100:
                        return


N, M = map(int, sys.stdin.readline().split())
visited = [0 for _ in range(101)]
step = [0 for _ in range(101)]
graph = [i for i in range(101)]

for _ in range(N + M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u] = v

bfs()

print(step[100])
