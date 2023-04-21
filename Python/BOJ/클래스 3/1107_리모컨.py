# gold 5
# 2956ms

# 고장난 버튼은 빼고, 남은 버튼으로 만들 수 있는 수 중
# N에 가장 가까운 값을 만들고
# 거기서 N을 뺀 절댓값이 답이다.

# 시작점이 100이라는 게 걸리는뎀
# edit

import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

error = list(map(int, sys.stdin.readline().split()))

button = abs(100 - N)

for num in range(1000001):
    num = str(num)
    l = len(num)

    for i in range(l):
        if int(num[i]) in error:
            break

        elif i == len(num) - 1:
            button = min(button, abs(int(num) - N) + l)

print(button)
