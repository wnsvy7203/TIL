# silver 2
# 108ms

from collections import deque

A, B = map(int, input().split())


def bfs(x):
    que = deque([(x, 1)])

    while que:
        temp, res = que.popleft()

        if temp == B:
            return res

        if temp <= B:
            que.append((temp * 2, res+1))
            que.append((temp * 10 + 1, res+1))

    return -1


print(bfs(A))
