# D4
# 686ms

from itertools import combinations

T = int(input())

for t in range(1, T+1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))

    minH = 10000 * 20 + 1
    for i in range(1, N+1):
        com = list(combinations(height, i))

        for j in com:
            tmp = sum(j)
            if B <= tmp < minH:
                minH = tmp

    print(f'#{t} {minH - B}')
