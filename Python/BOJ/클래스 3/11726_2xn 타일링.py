# silver 3
# 72ms

memo = [0 for _ in range(1001)]

for i in range(1, 4):
    memo[i] = i

for i in range(4, 1001):
    memo[i] = memo[i-1] + memo[i-2]

print(memo[int(input())] % 10007)
