import sys

n = int(sys.stdin.readline())
cnt = 0

for i in range(1, n+1):
    for j in range(1, n+1, i):
        cnt += 1

print(cnt)

# cnt = [0 for _ in range(n+1)]
# for i in range(1, n+1):
#     if n % i:
#         cnt[i] = cnt[i-1] + (n // i + 1)
#     else:
#         cnt[i] = cnt[i-1] + (n // i)
#
# print(cnt[n])
