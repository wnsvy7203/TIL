# silver 4
# 68ms

import sys

N, K = map(int, sys.stdin.readline().split())
value = [int(sys.stdin.readline()) for _ in range(N)]

k = K
cnt = 0

for i in range(N-1, -1, -1):
    if value[i] > k:
        continue
    else:
        cnt += k // value[i]
        k %= value[i]

        if k == 0:
            break

print(cnt)
