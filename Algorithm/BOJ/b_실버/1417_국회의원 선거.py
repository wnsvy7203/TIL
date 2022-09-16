# Silver 5
# 303ms

# 다솜 = 미친 정신병자, 기호 1번

import sys

input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
a = arr.pop(0)

cnt = 0
if arr:
    while a <= max(arr):
        a += 1
        cnt += 1
        arr[arr.index(max(arr))] -= 1

print(cnt)
