import sys
import heapq

N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(N)]
heap = []
heapq.heapify(heap)

for i in arr:
    if i:
        heapq.heappush(heap, i)
    else:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
