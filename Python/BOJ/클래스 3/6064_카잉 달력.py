# silver 1
# 4272ms

import sys
from math import lcm


T = int(sys.stdin.readline())

for _ in range(T):
    M, N, X, Y = map(int, sys.stdin.readline().split())

    x = X
    y = Y

    while x <= lcm(M, N):
        if x % N == y % N:
            print(x)
            break
        x += M
    else:
        print(-1)
