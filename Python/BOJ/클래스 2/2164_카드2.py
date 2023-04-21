# silver 4
# 228ms

from collections import deque
import sys

arr = deque(range(1, int(sys.stdin.readline())+1))

while arr:
    if len(arr) != 1:
        arr.popleft()
    else:
        print(arr[-1])
        break
    arr.rotate(-1)
