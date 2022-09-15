import heapq

arr = [8, 7, 6, 5, 4, 3, 2, 1]
heap = []

for i in arr:
    heapq.heappush(heap, i)

heapq.heapify(arr)

print(heap)
print(arr)
