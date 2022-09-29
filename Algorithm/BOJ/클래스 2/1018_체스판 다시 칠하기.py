# silver 4
# 132ms

import sys


def pattern_w(a, b):
    cnt = 0

    for y in range(8):
        if not y % 2:
            for x in range(0, 8, 2):
                if board[a+y][b+x] != 'W':
                    cnt += 1
            for x in range(1, 8, 2):
                if board[a+y][b+x] == 'W':
                    cnt += 1
        else:
            for x in range(0, 8, 2):
                if board[a+y][b+x] == 'W':
                    cnt += 1
            for x in range(1, 8, 2):
                if board[a+y][b+x] != 'W':
                    cnt += 1

    return cnt


def pattern_b(a, b):
    cnt = 0

    for y in range(8):
        if not y % 2:
            for x in range(0, 8, 2):
                if board[a+y][b+x] != 'B':
                    cnt += 1
            for x in range(1, 8, 2):
                if board[a+y][b+x] == 'B':
                    cnt += 1
        else:
            for x in range(0, 8, 2):
                if board[a+y][b+x] == 'B':
                    cnt += 1
            for x in range(1, 8, 2):
                if board[a+y][b+x] != 'B':
                    cnt += 1

    return cnt


def minimum(a, b):
    if pattern_w(a, b) > pattern_b(a, b):
        return pattern_b(a, b)
    else:
        return pattern_w(a, b)


N, M = map(int, sys.stdin.readline().split())
board = list(input() for _ in range(N))
minV = 65

for i in range(N-7):
    for j in range(M-7):
        if minimum(i, j) < minV:
            minV = minimum(i, j)

print(minV)
