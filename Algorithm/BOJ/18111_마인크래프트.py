# silver 2

import sys


N, M, B = map(int, sys.stdin.readline().split())
land = []
for _ in range(N):
    land += list(map(int, sys.stdin.readline().split()))

land.sort(reverse=True)

roof = max(land)
res = []
minV = float('inf')
for height in range(roof+1):
    b = B
    temp = land[:]
    flag = True
    cnt = 0
    for i in range(N*M):
        if temp[i] > height:
            while temp[i] > height:
                temp[i] -= 1
                b += 1
                cnt += 2

                if cnt > minV:
                    flag = False
                    break

        elif temp[i] < height:
            while b and temp[i] < height:
                b -= 1
                temp[i] += 1
                cnt += 1

                if cnt > minV:
                    flag = False
                    break

                if b == 0 and temp[i] < height:
                    flag = False
                    break

    if flag and cnt:
        res.append((cnt, height))
        if minV > cnt:
            minV = cnt

res.sort()

print(res[0][0], res[0][1])

# for i in range(len(res)):
#     if res[i][0] != 0:
#         print(res[i][0], res[0][1])
#         break
