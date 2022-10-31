# 고장난 버튼은 빼고, 남은 버튼으로 만들 수 있는 수 중
# N에 가장 가까운 값을 만들고
# 거기서 N을 뺀 절댓값이 답이다.

# 시작점이 100이라는 게 걸리는뎀

import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
error = [1 for _ in range(10)]
for _ in range(M):
    a = int(sys.stdin.readline())
    error[a] = 0

channel = 100

nums = [100000, 10000, 1000, 100, 10]

for i in nums:




