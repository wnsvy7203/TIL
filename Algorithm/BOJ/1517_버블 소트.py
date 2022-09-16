# Platinum 5

import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

cnt = 0

for i in range(1, N+1):
    if i < arr[i-1]:
        cnt += (i + 1 - arr[i])

print(cnt)
