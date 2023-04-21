# silver 4
# 72ms

import sys

N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split()))
P.sort(reverse=True)

res = 0
for i in range(N):
    res += sum(P[i:])

print(res)
