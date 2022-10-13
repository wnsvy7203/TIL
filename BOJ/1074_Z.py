N, r, c = map(int, input().split())
arr = [[0] * (1 << N) for _ in range(1 << N)]

cnt = 0

for y in range(0, 1 << N, 2):
    for x in range(0, 1 << N, 2):
        for i in range(y, y+2):
            for j in range(x, x+2):
                arr[i][j] = cnt
                cnt += 1

print(arr[c][r])
