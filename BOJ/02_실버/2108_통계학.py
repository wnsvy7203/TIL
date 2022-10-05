# silver 3
# 1452ms

from collections import defaultdict
import sys

N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(N)]

nums.sort()
print(round(sum(nums) / N))
print(nums[N//2])

dic = defaultdict(int)
app = []
for i in nums:
    dic[i] += 1

for key, value in dic.items():
    if value == max(dic.values()):
        app.append(key)
# for i in dic:
#     if i[-1] == max(dic.values()):
#         string += str(num.value)
print(app[1] if len(app) >= 2 else app[0])
print(nums[-1] - nums[0])
