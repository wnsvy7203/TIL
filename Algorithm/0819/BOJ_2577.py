# 숫자의 개수

arr = [int(input()) for _ in range(3)]

mul = 0
for i in range(3):
    mul = arr[0]*arr[1]*arr[2]

s = str(mul)
cnt = [0] * 10
for i in s:
    cnt[int(i)] += 1

for i in range(10):
    print(cnt[i])
