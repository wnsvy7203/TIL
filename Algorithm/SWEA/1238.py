# D4
# 173ms

def bfs(v):
    visited = [0] * 101                         # 방문 표시할 visited 선언
    queue = [v]                                 # 현재 위치를 표시할 queue, 최초 값은 파라미터
    visited[v] = 1                              # 현재 위치 방문 표시
    while queue:                                # queue 에 값이 있는 동안
        t = queue.pop(0)                        # queue 에서 값 pop(0)
        for a in adjList[t]:                    # adjList 에서 확인
            if not visited[a]:                  # 아직 방문하지 않았으면
                queue.append(a)                 # 현재 위치 갱신
                visited[a] = visited[t] + 1     # 몇 단계째인지 표시

    idx = []                                    # visited 가 가장 큰 인덱스를 찾을 리스트 idx 선언

    for b in range(101):
        if visited[b] == max(visited):          # visited 중 가장 큰 값을 찾는 문제
            idx.append(b)                       # idx 에 해당 인덱스 append

    return max(idx)                             # idx 에 여러 값이 있는 경우, 가장 큰 값이 정답


for tc in range(1, 11):
    N, start = map(int, input().split())
    arr = list(map(int, input().split()))

    adjList = [[] for _ in range(101)]          # 각 노드마다 이어진 노드를 표시하기 위한 adjList 선언

    for i in range(0, N, 2):                    # 범위를 반복하면서
        if arr[i+1] not in adjList[arr[i]]:     # 중복되는 경우가 있고, 결과는 같다는 제약 조건 구현
            adjList[arr[i]].append(arr[i+1])
    print(f'#{tc} {bfs(start)}')                # 시작점을 파라미터로 하는 bfs 함수 소환
