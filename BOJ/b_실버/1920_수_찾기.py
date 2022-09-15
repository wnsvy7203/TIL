# 1 <= N <= 100000
# 1 <= M <= 100000

import sys

N = int(sys.stdin.readline())
A = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
arr_M = list(map(int, sys.stdin.readline().split()))

for i in arr_M:
    s = 0
    e = N-1
    while s <= e:
        idx = (s+e) // 2
        if i == A[idx]:
            print(1)
            break
        elif i > A[idx]:
            s = idx + 1
        else:
            e = idx - 1

        if s > e:
            print(0)

