# silver 2
# 84ms

import sys


def check(r, c, n):
    start = paper[r][c]

    for i in range(r, r+n):
        for j in range(c, c+n):
            if paper[i][j] != start:
                for a in range(2):
                    for b in range(2):
                        check(r + a*(n//2), c + b*(n//2), n//2)
                else:
                    return

    if start == 0:
        cnt[0] += 1
    else:
        cnt[1] += 1


N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

cnt = [0] * 2
check(0, 0, N)

print(cnt[0])
print(cnt[1])
