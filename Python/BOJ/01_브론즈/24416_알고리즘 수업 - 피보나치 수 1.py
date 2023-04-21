# bronze 1
# 72ms

N = int(input())

cnt = 0
cntF = 0

dp = [0 for _ in range(41)]
dp[1] = dp[2] = 1

for i in range(3, N+1):
    dp[i] = dp[i-1] + dp[i-2]
    cntF += 1

print(dp[N], cntF)
