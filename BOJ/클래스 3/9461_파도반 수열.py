# silver 3
# 76ms

memo = [1 for _ in range(101)]

for i in range(4, 101):
    memo[i] = memo[i-2] + memo[i-3]

for _ in range(int(input())):
    print(memo[int(input())])
