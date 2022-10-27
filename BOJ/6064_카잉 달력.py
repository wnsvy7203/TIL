import sys
from math import gcd, lcm


T = int(sys.stdin.readline())

for _ in range(T):
    M, N, X, Y = map(int, sys.stdin.readline().split())

    x = 1
    y = 1
    cnt = 1

    for i in range(1, lcm(M, N)):
        if x == X and y == Y:
            print(i)
            break

        if x == M:
            x = 1
        else:
            x += 1

        if y == N:
            y = 1
        else:
            y += 1
    else:
        print(-1)
