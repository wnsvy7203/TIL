# silver 2
# 6160ms

import sys


def check(r, c, n):
    start = paper[r][c]

    for i in range(r, r+n):
        for j in range(c, c+n):
            if paper[i][j] != start:
                for a in range(3):
                    for b in range(3):
                        check(r + a*(n//3), c + b*(n//3), n//3)
                # n 이 3의 제곱수로 표현될 때, 예처럼 9일 때
                # paper[0][0] != paper[0][3]면 paper[0][1]과 paper[0][3]을 비교할 필요가 없으므로,
                # for 문을 다 돌면 return 해서 불필요한 과정을 줄인다.
                # return하지 않으면 계속 비교하면서 종이의 개수를 계속 업데이트한다.
                else:
                    return

    if start == -1:
        cnt[-1] += 1
    elif start == 0:
        cnt[0] += 1
    else:
        cnt[1] += 1


N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

cnt = [0] * 3
check(0, 0, N)

print(cnt[-1])
print(cnt[0])
print(cnt[1])
