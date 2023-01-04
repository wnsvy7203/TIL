from collections import deque

A, B = map(int, input().split())


def bfs(x):
    visited = [0] * (B + 100)
    que = deque([(x, 0)])

    while que:
        temp, res = que.popleft()

        if temp == B:
            return res

        if temp < B:
            que.append((temp * 2, res))
            que.append((temp * 10 + 1, res))

        if temp > B:
            return -1


print(bfs(A))
