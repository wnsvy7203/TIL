import sys
from collections import deque


def bfs():
    queue = deque([0])

    while queue:
        v = queue.popleft()
        for w in graph[v]:
            if visited[w] == -1:
                queue.append(w)
                visited[w] = visited[v] + 1


N = int(sys.stdin.readline())
graph = [[] for _ in range(N)]
visited = [-1 for _ in range(N)]
visited[0] = 0

for _ in range(N-1):
    U, V = map(int, sys.stdin.readline().split())
    graph[U].append(V)

goal = int(sys.stdin.readline())

bfs()

print(visited)
while max(visited) > goal:
    if visited.index(max(visited)) in visited.index(max(visited) - 1):
        pass