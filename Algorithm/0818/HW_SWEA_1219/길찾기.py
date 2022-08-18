def dfs(s):                                   # 시작점만 파라미터로 받으면 된다.
    top = 0                                   # top 초기화
    visited[s] = 1                            # 시작점 방문 표시
    while True:
        for w in adjList[s]:
            if visited[w] == 0:               # 아직 방문한 적이 없으면,
                top += 1                      # top 을 1 추가한다.
                stack[top] = s                # 스택에 현재 위치를 표시해준다.
                s = w                         # 위치 갱신
                visited[w] = 1                # 현재 위치를 방문했음을 표시
                break
        else:                                 # for 문을 모두 돌았을 때, 더 이상 앞으로 진행할 수 없다면
            if top != 0:                      # 한 단계 전으로 돌아온다.
                s = stack[top]                # s도 뒤로
                top -= 1                      # top 도 하나 뒤로
            else:
                break

    if visited[99] == 1:                      # 함수가 종료되는 시점에 99를 방문한 적이 있다면
        return 1                              # 1 반환
    else:
        return 0                              # 아니면 0 반환


for tc in range(1, 11):
    N, E = map(int, input().split())
    adjList = [[] for _ in range(100)]
    arr = list(map(int, input().split()))     # 간선 입력

    for i in range(0, 2*E, 2):
        adjList[arr[i]].append(arr[i+1])      # 단방향 간선임을 감안하여, adjList 에 옮긴다.

    visited = [0] * 100                       # 방문 여부 확인
    stack = [0] * 100                         # stack 으로 현재 위치 확인

    print(f'#{tc} {dfs(0)}')                  # 시작점은 반드시 0이다.
