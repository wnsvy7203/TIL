# silver 3
# 0ms

import sys

N = int(sys.stdin.readline())
step = [0 for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
for i in range(1, N+1):
    step[i] = int(sys.stdin.readline())

score = step[N]
visited[N] = 1
n = N
while n > 0:
    if step[n-1] >= step[n-2]:
        score += step[n-1]
    else:
        score
