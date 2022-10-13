# silver 2
# 784ms

import sys


def dfs(root):
    stk = [root]
    visited[root] = 1

    while stk:
        v = stk.pop()

        for w in graph[v]:
            if not visited[w]:
                visited[w] = 1
                stk.append(w)


N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0

for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)
