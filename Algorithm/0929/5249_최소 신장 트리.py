# D4
# 119ms

def prim(r, V):
    mst = [0] * N                               # mst 포함 여부
    mst[r] = 1
    s = 0
    for _ in range(V):
        n1 = 0
        minV = 11
        for i in range(N):
            if mst[i] == 1:
                for j in range(N):
                    if 0 < adjM[i][j] < minV and mst[j] == 0:
                        n1 = j
                        minV = adjM[i][j]

        s += minV
        mst[n1] = 1
    return s


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    N = V + 1
    adjM = [[0] * N for _ in range(N)]
    adjL = [[] for _ in range(N)]
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        adjM[n1][n2] = w
        adjM[n2][n1] = w
        adjL[n1].append((n2, w))
        adjL[n2].append((n1, w))

    print(f'#{tc} {prim(0, V)}')
