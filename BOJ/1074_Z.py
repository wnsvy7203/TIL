def check(r, c, n):
    cnt = 0
    start = paper[r][c]

    for i in range(r, r+n):
        for j in range(c, c+n):
            if paper[i][j] != start:
                for a in range(2):
                    for b in range(2):
                        check(r + a*(n//2), c + b*(n//2), n//2)
                else:
                    return

    return cnt


N, r, c = map(int, input().split())
arr = [[0] * (1 << N) for _ in range(1 << N)]

cnt = 0

for y in range(0, 1 << N, 2):
    for x in range(0, 1 << N, 2):
        pass
print(arr[c][r])