# silver 4
# 68ms

import sys

N, K = map(int, sys.stdin.readline().split())
cnt = 0
era = [0] * (N+1)
visited = [0] * (N+1)

for i in range(2, N+1):
    if visited[i]:
        continue
    else:
        for j in range(i, N+1, i):
            if visited[j]:
                continue
            else:
                cnt += 1
                visited[j] = 1
                era[j] = cnt

                if cnt == K:
                    print(j)
                    break
