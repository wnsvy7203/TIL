N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort()

roof_left = 0
roof_right = 0

idx_left = 0
idx_right = N - 1
for i in range(N):
    if arr[i][1] > roof_left:
        roof_left = arr[i][1]
        idx_left = i
for i in range(N-1, -1, -1):
    if arr[i][1] > roof_right:
        roof_right = arr[i][1]
        idx_right = i

answer = 0

left = arr[:idx_left+1]
for i in range(1, len(left)):
    if left[i][1] < left[i-1][1]:
        left[i][1] = left[i-1][1]
    answer += left[i-1][1] * (left[i][0] - left[i - 1][0])

right = list(reversed(arr[idx_right:]))

for i in range(1, len(right)):
    if right[i][1] < right[i-1][1]:
        right[i][1] = right[i-1][1]
    answer += right[i-1][1] * (right[i-1][0] - right[i][0])

if idx_left == idx_right:
    answer += roof_left
else:
    answer += roof_left*(right[-1][0] - left[-1][0] + 1)

print(answer)
