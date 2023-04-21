# gold 2
# 784ms

import sys
from collections import deque


def dfs():
    visited = [-1 for _ in range(N)]
    visited[1] = 0

    stk = deque([1])
    while stk:
        x = stk.popleft()

        for y, z in graph[x]:
            if visited[y] == -1:
                visited[y] = visited[x] + z
                stk.append(y)

    return visited.index(max(visited))


def find(n):
    visited = [-1 for _ in range(N)]
    visited[n] = 0

    que = deque([n])
    while que:
        i = que.popleft()

        for j, k in graph[i]:
            if visited[j] == -1:
                visited[j] = visited[i] + k
                que.append(j)

    return max(visited)


V = int(sys.stdin.readline())

N = V+1
graph = [[] for _ in range(N)]

for _ in range(V):
    base = deque(map(int, sys.stdin.readline().split()))
    node = base.popleft()
    while base != deque([-1]):
        v = base.popleft()
        w = base.popleft()

        graph[node].append((v, w))

print(find(dfs()))
