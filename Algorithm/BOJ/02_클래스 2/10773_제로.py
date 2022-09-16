# Silver 4
# 116ms

import sys

K = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(K)]
new_arr = []
for i in range(K):
    if arr[i] != 0:
        new_arr.append(arr[i])
    else:
        new_arr.pop()
print(sum(new_arr))
