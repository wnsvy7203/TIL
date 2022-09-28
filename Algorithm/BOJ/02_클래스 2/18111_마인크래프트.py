# silver 2
# 476ms

import sys

N, M, B = map(int, sys.stdin.readline().split())
land = []

for _ in range(N):
    land += list(map(int, sys.stdin.readline().split()))

bottom, top = min(land), max(land)

minV = float('inf')
res = 0

for height in range(bottom, top + 1):
    s = 0
    e = 0
    for i in range(N*M):
        if land[i] >= height:
            e += land[i] - height
        else:
            s += height - land[i]

    if s > e + B:
        continue

    cnt = s + (e * 2)
    if cnt <= minV:
        minV = cnt
        res = height

print(minV, res)