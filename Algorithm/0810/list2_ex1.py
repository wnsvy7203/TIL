N = 3 # 행
M = 4 # 열
# N개의 원소를 갖는 0으로 초기화된 1차원 배열
arr1 = [0] * N

# 크기가 N * M이고 0으로 초기화된 2차원 배열
arr2 = [[0] * M for _ in range(N)]

# arr3 = [[0]*M]*N
# arr3[0][0] = 1 # 이 경우는 2차원 배열을 만든 것이 아니라, M개의 원소를 갖는, 0으로 초기화된 1차원 배열을 여러 개 만든 것이기 때문에, [1, 0, 0, 0] 3개를 갖는다.
