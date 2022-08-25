def bfs(s, g):
    queue = [s]                                     # 시작점을 담은 queue
    visited[s] = 0                                  # 거리를 나타내는 변수가 되는 것이지.

    while queue:                                    # queue 에 값이 있을 때까지
        s = queue.pop(0)                            # 시작점 확인
        for w in adjList[s]:                        # 시작점에 연결된 간선 확인
            if visited[w] == 0:                     # 다음 노드 확인
                queue.append(w)                     # 해당 노드를 queue 에 더하고,
                visited[w] = visited[s] + 1         # 거리를 업데이트 해 준다.

    return visited[g]                               # 시작점 s 부터 g 까지의 거리를 반환, or 갈 수 없다면 0 반환


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    N = V + 1
    adjList = [[] for _ in range(N)]                # 간선을 담을 adjList 초기화
    visited = [0] * N
    for _ in range(E):
        a, b = map(int, input().split())            # 주어진 간선을 입력
        adjList[a].append(b)
        adjList[b].append(a)

    s, g = map(int, input().split())
    print(f'#{tc} {bfs(s, g)}')
