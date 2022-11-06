import sys
import heapq

T = int(sys.stdin.readline())

for _ in range(T):
    k = int(sys.stdin.readline())

    maxQ = []
    minQ = []
    visited = [0 for _ in range(k)]

    for i in range(k):
        get = tuple(sys.stdin.readline().split())
        a = get[0]
        b = int(get[1])

        if a == 'I':
            heapq.heappush(maxQ, (-b, i))
            heapq.heappush(minQ, (b, i))
            visited[i] = 1
        elif a == 'D':
            if b == -1:
                while minQ and not visited[minQ[0][1]]:
                    heapq.heappop(minQ)
                if minQ:
                    x, y = heapq.heappop(minQ)
                    visited[y] = 0
            else:
                while maxQ and not visited[maxQ[0][1]]:
                    heapq.heappop(maxQ)
                if maxQ:
                    x, y = heapq.heappop(maxQ)
                    visited[y] = 0

    while maxQ and not visited[maxQ[0][1]]:
        heapq.heappop(maxQ)
    while minQ and not visited[minQ[0][1]]:
        heapq.heappop(minQ)

    if maxQ and minQ:
        print(-heapq.heappop(maxQ)[0], heapq.heappop(minQ)[0])
    else:
        print('EMPTY')
