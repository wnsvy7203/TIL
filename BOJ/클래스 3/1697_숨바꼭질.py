# silver 1
# 148ms

from collections import deque


def bfs(n):
    visited = [0] * 100001
    queue = deque([n])
    visited[n] = 1
    while queue:
        v = queue.popleft()

        if v == K:
            return visited[v]-1

        for w in [v-1, v+1, 2*v]:
            if 0 <= w <= 100000 and not visited[w]:
                queue.append(w)
                visited[w] = visited[v] + 1


N, K = map(int, input().split())

print(bfs(N))
