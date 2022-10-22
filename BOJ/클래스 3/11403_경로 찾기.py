# silver 1
# 88ms

import sys


def find(x):
    visited = [0 for _ in range(N)]

    stk = [x]

    while stk:
        v = stk.pop()

        for w in graph[v]:
            if not visited[w]:
                visited[w] = 1
                stk.append(w)

    return visited


N = int(sys.stdin.readline())

node = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

graph = [[] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if node[i][j] == 1:
            graph[i].append(j)

for i in range(N):
    print(*find(i))
