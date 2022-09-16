# Bronze 1
# 72ms

import sys

N, M = map(int, sys.stdin.readline().split())

gcd = 0
lcm = 0
if N <= M:
    for i in range(N, 0, -1):
        if N % i == 0 and M % i == 0:
            gcd = i
            break
    j = M
    while True:
        if j % N == 0:
            lcm = j
            break
        else:
            j += M
else:
    for i in range(N, 0, -1):
        if N % i == 0 and M % i == 0:
            gcd = i
            break
    j = N
    while True:
        if j % M == 0:
            lcm = j
            break
        else:
            j += N
print(gcd)
print(lcm)
