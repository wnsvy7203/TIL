# silver 2
# 108ms

import sys

K, N = map(int, sys.stdin.readline().split())
length = [int(sys.stdin.readline()) for _ in range(K)]
end = sum(length) // N
start = 1

while start <= end:
    mid = (start + end) // 2
    plus = 0

    for k in length:
        plus += k // mid

    if plus >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)
