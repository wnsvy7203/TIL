# silver 3
# 68ms

# 2번 연속으로는 밟을 수 있다.
# 현재 위치가 step[i]일 때 가능한 경우의 수를 구분해보면,
# 1. step[i-3], step[i-2]를 밟고 온 경우
# 2. step[i-3], step[i-1]를 밟고 온 경우
import sys

N = int(sys.stdin.readline())
step = [0] + [int(sys.stdin.readline()) for _ in range(N)] + [0]
dp = [0 for _ in range(N+2)]

dp[1] = step[1]
dp[2] = dp[1] + step[2]

for i in range(3, N+1):
    dp[i] = max(dp[i-3] + step[i-1], dp[i-2]) + step[i]

print(dp[-2])
