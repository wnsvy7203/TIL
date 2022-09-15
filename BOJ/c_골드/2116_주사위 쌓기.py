# Gold 4
# 776ms

# 0, 5 / 1, 3 / 2, 4 로 이어진다.
from copy import deepcopy

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

order = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}                    # 다음 순서 확인

my_max = []

for i in range(6):
    dice = deepcopy(arr)                                        # 매번 새롭게 확인해야 한다.
    result = 0
    r = 0
    c = i
    while r < N:
        delete = dice[r][order[c]]
        dice[r][c] = 0
        dice[r][order[c]] = 0
        result += max(dice[r])

        if r+1 == N:
            break
        else:
            c = dice[r+1].index(delete)
        r += 1
    my_max.append(result)
print(max(my_max))
