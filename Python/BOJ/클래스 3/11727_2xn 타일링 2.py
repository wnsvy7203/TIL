memo = [0 for _ in range(1001)]

memo[1] = 1
memo[2] = 3

for i in range(3, 1001):
    memo[i] = 2 * memo[i-2] + memo[i-1]

print(memo[int(input())] % 10007)
