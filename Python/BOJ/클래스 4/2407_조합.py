# silver 3
# 36ms

N, M = map(int, input().split())

n = 1
m = 1

for i in range(N, N-M, -1):
    n *= i

for i in range(M, 0, -1):
    m *= i

print(n // m)
