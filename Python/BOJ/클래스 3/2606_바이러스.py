# silver 3
# 68ms

import sys


def dfs(v):
    cnt = 0
    visited = [0] * (N+1)
    visited[v] = 1

    top = -1
    stk = [0] * (N + 1)
    while True:
        for w in adjList[v]:
            if visited[w] == 0:
                top += 1
                stk[top] = v
                v = w
                visited[w] = 1
                cnt += 1
                break
        else:
            if top != -1:
                v = stk[top]
                top -= 1
            else:
                break

    return cnt


N = int(sys.stdin.readline())
E = int(sys.stdin.readline())

Edge = [list(map(int, sys.stdin.readline().split())) for _ in range(E)]
adjList = [[] for _ in range(N+1)]

for i in range(E):
    adjList[Edge[i][0]].append(Edge[i][1])
    adjList[Edge[i][1]].append(Edge[i][0])

print(dfs(1))
