# silver 5
# 72ms

import sys

N = int(sys.stdin.readline())
cnt2 = 0
cnt5 = 0
for i in range(2, N+1):
    if i % 2 == 0:
        f2 = i
        while f2 % 2 == 0:
            cnt2 += 1
            f2 //= 2
    if i % 5 == 0:
        f5 = i
        while f5 % 5 == 0:
            cnt5 += 1
            f5 //= 5

print(min(cnt2, cnt5))
