'''
6 10
1 2 2
1 3 5
1 4 3
2 3 7
2 6 10
3 4 1
3 5 2
3 6 5
4 5 7
5 6 2
'''


def dijkstra(s):
    used = [0] * N                     # 비용이 결정된 정점을 표시
    used[s] = 1                        # 출발점 비용 결정
    for ii in range(N):
        D[ii] = adjM[s][ii]

    # 남은 정점의 비용 결정
    for _ in range(V):              # 남은 정점 개수만큼 반복
        # D[ww]가 최소인 ww 결정, 비용이 결정되지 않은 정점 ww 중에서
        min_v = INF
        ww = 0
        for ii in range(N):
            if not used[ii] and min_v > D[ii]:
                min_v = D[ii]
                ww = ii
        used[ww] = 1                # 비용 결정
        for vv in range(N):
            if 0 < adjM[ww][vv] < INF:
                D[vv] = min(D[vv], D[ww]+adjM[ww][vv])


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
dijkstra(1)
print(D)
