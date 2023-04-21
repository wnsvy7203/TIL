# bronze 1
# 88ms

T = int(input())

for tc in range(1, T+1):
    k = int(input())    # 1 <= k, n <= 14
    n = int(input())

    arr = [[0] * n for _ in range(k+1)]
    for i in range(n):
        arr[0][i] = i + 1

    for i in range(1, k+1):
        for j in range(n):
            arr[i][j] = arr[i-1][0]
            for a in range(1, j+1):
                arr[i][j] += arr[i-1][a]

    print(arr[k][n-1])


