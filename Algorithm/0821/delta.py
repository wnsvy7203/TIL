di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N = 3
M = 4
arr = [[1, 2, 3, 4], [4, 5, 6, 8]]
# for i in range(N):
#     for j in range(M):
#         for k in range(4):
#             ni = i + di[k]
#             nj = j + dj[k]
#             if 0 <= ni < N and 0 <= nj < M:
#                 print(ni, nj)

# for i in range(N):
#     for j in range(M):
#         for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
#             mi, mj = i + di, j + dj
#             if 0 <= mi < N and 0 <= mj < M:
#                 print(mi, mj)

# 인접 2개의 배열 요소를 탐색하려면
for i in range(N):
    for j in range(M):
        for k in range(4):
            for d in range(1, 3):
                li = i + (di[k] * d)
                lj = j + (dj[k] * d)
                if 0 <= li < N and 0 <= lj < M:
                    print(li, lj)
