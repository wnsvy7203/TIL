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


def dijkstra(s, V):
    U = [0]*(V+1)       # 비용이 결정된 정점을 표시
    U[s] = 1            # 출발점 비용 결정
    for i in range(V+1):
        D[i] = adjM[s][i]

    # 남은 정점의 비용 결정
    for _ in range(V):      # 남은 정점 개수만큼 반복
        # D[w]가 최소인 w 결정, 비용이 결정되지 않은 정점w 중에서
        minV = INF
        w = 0
        for i in range(V+1):
            if U[i] == 0 and minV > D[i]:
                minV = D[i]
                w = i
        U[w] = 1                # 비용 결정
        for v in range(V+1):
            if 0 < adjM[w][v] < INF:
                D[v] = min(D[v], D[w]+adjM[w][v])


INF = 10000
N, M, K, X = map(int, input().split())
adjM = [[INF]*(N+1) for _ in range(N+1)]
for i in range(N+1):
    adjM[i][i] = 0
for _ in range(M):
    u, v, w = map(int, input().split())
    adjM[u][v] = w

D = [0]*(N+1)
dijkstra(0, N)
print(D)
