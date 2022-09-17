# Silver 2
# 88ms

import sys


def dfs(v):
    visited = [0] * (N+1)
    stk = [0] * (N+1)
    top = -1
    dfs_list = [v]

    visited[v] = 1
    while True:
        for w in adjList[v]:
            if visited[w] == 0:
                top += 1
                stk[top] = v
                v = w
                dfs_list.append(v)
                visited[w] = 1
                break
        else:
            if top != -1:
                v = stk[top]
                top -= 1
            else:
                break
    return dfs_list


def bfs(v):
    visited = [0] * (N+1)
    queue = [v]
    visited[v] = 1

    bfs_list = []
    while queue:
        v = queue.pop(0)
        bfs_list.append(v)
        for w in adjList[v]:
            if visited[w] == 0:
                queue.append(w)
                visited[w] = 1
    return bfs_list


N, M, V = map(int, sys.stdin.readline().split())
Edge = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
adjList = [[] for _ in range(N + 1)]

for i in range(M):
    adjList[Edge[i][0]].append(Edge[i][1])
    adjList[Edge[i][1]].append(Edge[i][0])

for i in adjList:
    i.sort()

print(*dfs(V))
print(*bfs(V))
