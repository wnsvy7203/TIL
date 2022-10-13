N = int(input())

six = [1 for _ in range(707)]
for i in range(1, 707):
    six[i] = six[i-1] + (4*i + 1)

dp = [float('inf')] * 1000001
for i in range(6):
    dp[i] = i

for i in six:
    dp[i] = 1

for i in range(7, 1000001):
    pass
