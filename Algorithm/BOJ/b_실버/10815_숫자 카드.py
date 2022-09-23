# Silver 5
# 3644ms

import sys

M = int(sys.stdin.readline())
check = list(map(int, sys.stdin.readline().split()))
N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))

check.sort()
check_list = []

# for i in range(N):
#     for j in check:
#         if j == card[i]:
#             check_list[i] = 1
#             break

for card in cards:
    start = 0
    end = M - 1
    while start <= end:
        mid = (start + end) // 2
        if card > check[mid]:
            start = mid + 1
        elif card < check[mid]:
            end = mid - 1
        else:
            check_list.append('1')
            break

        if start > end:
            check_list.append('0')
# else:
#     for i in range(N):
#         if type(card_list[i]) == int:
#             card_list[i] = False
#
#
# for i in range(N):
#     if card_list[i]:
#         card_list[i] = 1
#     else:
#         card_list[i] = 0
print(*check_list)
