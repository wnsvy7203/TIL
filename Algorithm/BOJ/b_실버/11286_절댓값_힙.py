# Silver 1
# 184ms

import sys
import heapq

N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(N)]
heap = []

for i in arr:
    if i:
        heapq.heappush(heap, [abs(i), i])
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
