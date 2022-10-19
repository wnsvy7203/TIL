# D3
# 116ms

from itertools import combinations


def baby_gin(arr):
    flag = False
    for a in combinations(arr, 3):
        a = sorted(list(a))
        if a[0] == a[1] == a[2]:
            flag = True
        if a[0] + 1 == a[1] and a[1] + 1 == a[2]:
            flag = True
    return flag


T = int(input())

for tc in range(1, T+1):
    card = list(map(int, input().split()))

    first = []
    second = []

    for i in range(0, 12, 2):
        first.append(card[i])
        second.append(card[i+1])

        if len(first) >= 3:
            if baby_gin(first):
                print(f'#{tc} 1')
                break
            if baby_gin(second):
                print(f'#{tc} 2')
                break
    else:
        print(f'#{tc} 0')
