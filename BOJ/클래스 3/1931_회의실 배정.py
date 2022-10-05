# silver 1
# 384ms
import sys
from collections import deque

N = int(sys.stdin.readline())
time = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(N)])
time.sort(key=lambda x: x[1])
time = deque(time)

res = [time.popleft()]

while time:
    home = res[-1][1]
    next_truck = time.popleft()
    next_start = next_truck[0]

    if home <= next_start:
        res.append(next_truck)

print(len(res))
