# bronze 2
# 76ms

arr = [int(input()) for _ in range(10)]
cnt = [0] * 42
result = 0
for i in arr:
    cnt[i % 42] += 1

for i in range(42):
    if cnt[i]:
        result += 1

print(result)
