'''
5 11
0 1 3
0 2 5
1 2 2
1 3 6
2 1 1
2 3 4
2 4 6
3 4 2
3 5 3
4 0 3
4 5 6
'''


def dijkstra(s):
    U = [0] * N                     # 비용이 결정된 정점을 표시
    U[s] = 1                        # 출발점 비용 결정
    for i in range(N):
        D[i] = adjM[s][i]

    # 남은 정점의 비용 결정
    for _ in range(V):              # 남은 정점 개수만큼 반복
        # D[w]가 최소인 w 결정, 비용이 결정되지 않은 정점 w 중에서
        minV = INF
        w = 0
        for i in range(N):
            if not U[i] and minV > D[i]:
                minV = D[i]
                w = i
        U[w] = 1                # 비용 결정
        for v in range(N):
            if 0 < adjM[w][v] < INF:
                D[v] = min(D[v], D[w]+adjM[w][v])


INF = 10000
V, E = map(int, input().split())    # V: 정점 개수, E: 간선 개수
N = V + 1

adjM = [[INF] * N for _ in range(N)]

for i in range(N):
    adjM[i][i] = 0                  # 자기 자신에서 출발해서 다시 들어가는 경우는 확인 불필요.
for _ in range(E):                  # 간선의 개수만큼
    u, v, w = map(int, input().split())
    adjM[u][v] = w                  # 인접행렬 확인, 가중치 저장

D = [0] * N
dijkstra(0)
print(D)
