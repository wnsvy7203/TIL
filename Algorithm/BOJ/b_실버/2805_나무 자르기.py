# Silver 2
# 3612ms

import sys

N, M = map(int, sys.stdin.readline().split())
height = list(map(int, sys.stdin.readline().split()))

s = 0
e = max(height)

while True:
    m = (s + e) // 2
    w = 0

    w = sum(i - m if i - m > 0 else 0 for i in height)

    if w >= M:
        s = m + 1
    else:
        e = m - 1

    if s > e:
        print(e)
        break
