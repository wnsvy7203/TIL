# silver 2
# 352ms

import sys


def find():
    stk = [1]

    while stk:
        v = stk.pop()

        for w in graph[v]:
            if not visited[w]:
                visited[w] = 1
                parents[w] = v
                stk.append(w)


N = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [0 for _ in range(N+1)]
parents = [0 for _ in range(N+1)]

visited[1] = 1

find()

for i in range(2, N+1):
    print(parents[i])
