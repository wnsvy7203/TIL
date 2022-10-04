from itertools import combinations

arr = [1, 2, 3]
result = []

# 1: combinations 메소드 사용(시간복잡도: O(n * nCr))
# for i in range(len(arr)+1):
#     result += list(combinations(arr, i))

# 2: 단순 반복문과 배열(시간복잡도: O(n * 2^n)
# result += [[]]
# for num in arr:
#     n = len(result)
#     for x in range(n):
#         result.append(result[x]+[num])

# 3: 비트 연산(시간복잡도: O(n * 2^n)
for i in range(1 << len(arr)):
    subset = []
    for j in range(len(arr)):
        if i & (1 << j):
            subset.append(arr[j])
    result.append(subset)

print(result)
