# 별 3개
# 0ms

import sys

H, K, R = map(int, sys.stdin.readline().split())
works = [[] for _ in range(2 ** (H+1))]

for i in range(1, 2 ** H):
    works[i] = [[], []]

for i in range(2 ** H, 2 ** (H+1), 1):
    works[i] = list(map(int, sys.stdin.readline().split()))

day = 1
res = 0

while day <= R:
    day += 1

    if not day % 2:
        if works[1][0]:
            res += works[1][0].pop(0)
    else:
        if works[1][1]:
            res += works[1][1].pop(0)

    if not day % 2:
        for i in range(2, 2 ** H, 1):
            if works[i][0]:
                works[i // 2][0].append(works[i][0].pop(0))
    else:
        for i in range(2, 2 ** H, 1):
            if works[i][1]:
                works[i // 2][1].append(works[i][1].pop(0))

    for i in range(2 ** H, 2 ** (H+1), 1):
        if not i % 2:
            works[i // 2][0].append(works[i].pop(0))
        else:
            works[i // 2][1].append(works[i].pop(0))

print(res)
