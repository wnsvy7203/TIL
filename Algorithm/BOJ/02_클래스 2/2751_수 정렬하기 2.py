# silver 5
# 1348ms

import sys
input = sys.stdin.readline

N = int(input()) # 1 <= N <= 100000

arr = [int(input()) for _ in range(N)]

arr.sort()

for i in range(N):
    print(arr[i])
