T = int(input())
for x in range(1, T+1):
    # N: 크기, M: 개수, C: 최대 채취량
    N, M, C = map(int, input().split())
    bee = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]


