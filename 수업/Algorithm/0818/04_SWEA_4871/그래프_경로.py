T = int(input())


def dfs(s, g):                              # 시작점과 목적지를 파라미터로 사용
    top = 0                                 # top 초기화
    visited[s] = 1                          # 시작점 방문 표시
    while True:
        for w in adjList[s]:
            if visited[w] == 0:             # 아직 방문한 적이 없으면,
                top += 1                    # top 을 1 추가한다.
                stack[top] = s              # 스택에 현재 위치를 표시해준다.
                s = w                       # 위치 갱신
                visited[w] = 1              # 현재 위치를 방문했음을 표시
                break
        else:                               # for 문을 모두 돌았을 때, 더 이상 앞으로 진행할 수 없다면
            if top != 0:                    # 한 단계 전으로 돌아온다.
                s = stack[top]              # s도 뒤로
                top -= 1                    # top 도 하나 뒤로
            else:
                break

    if visited[g] == 1:                     # 함수가 종료되는 시점에 g를 방문한 적이 있다면
        return 1                            # 1 반환
    else:
        return 0                            # 아니면 0 반환


for tc in range(1, T + 1):
    V, E = map(int, input().split())        # V는 노드 개수, E는 간선 개수
    N = V + 1                               # 0은 포함되지 않으므로, 1 더해줘야 인덱스가 맞아떨어진다.
    adjList = [[] for _ in range(N)]
    for _ in range(E):
        a, b = map(int, input().split())    # 간선을 모두 입력받는다.
        adjList[a].append(b)                # 양방향 간선이 아니라, 단방향 간선이므로

    visited = [0] * N                       # 방문 여부 확인
    stack = [0] * N                         # stack 으로 현재 위치 확인

    S, G = map(int, input().split())        # 시작점과 목적지 입력

    print(f'#{tc} {dfs(S, G)}')
