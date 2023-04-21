# gold 4
# pypy 로만 제출 가능 - 3976ms

# 육각수는 1, 6, 15, 28, ... 등으로 진행된다.
# 단계를 거쳐 넘어오는 dp 문제이기 때문에,
# 만약 육각수를 더해 어떤 숫자가 나온다면 앞의 숫자에서 1단계 추가로 움직였다는 것을 표현해주면 된다.


N = int(input())

six = [0 for _ in range(710)]
for i in range(710):
    six[i] = (i+1) * (2*i + 1)  # 1000000 보다 작은 모든 육각수를 담는다.

# 1000000 보다 작은 육각수를 담았더니, 틀렸다고 뜬다. 왜지?
# 1000000 보다 조금 큰 것 몇 개를 추가했더니 맞았다.

dp = [float('inf')] * 1000001

for i in range(6):
    dp[i] = i

for i in range(6, N+1):
    for j in six:
        if j > i:               # j가 i보다 크면 확인할 필요가 없다.
            break
        if dp[i] > dp[i-j]:
            dp[i] = dp[i-j] + 1

print(dp[N])
