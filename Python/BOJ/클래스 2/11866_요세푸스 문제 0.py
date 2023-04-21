# silver 5
# 96ms

from collections import deque

N, K = map(int, input().split())
arr = deque(range(1, N+1))
new_arr = []
while arr:
    arr.rotate(-(K-1))
    new_arr.append(str(arr.popleft()))
result = ', '.join(new_arr)
print(f"<{', '.join(new_arr)}>")
