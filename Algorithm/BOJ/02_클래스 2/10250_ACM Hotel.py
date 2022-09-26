# bronze 2
# 140ms

for _ in range(int(input())):
    H, W, N = map(int, input().split())

    hotel = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            hotel[i][j] = (i+1) * 100 + j+1

    print(hotel[(N-1) % H][(N-1) // H])
