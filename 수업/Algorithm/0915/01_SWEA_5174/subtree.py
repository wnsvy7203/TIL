# 146ms

T = int(input())


def tree(n):
    global cnt                                  # 전역 변수 cnt 호출

    if ch1[n]:                                  # ch1[n]가 0이 아니면, 즉, 연결된 자식 노드가 있으면
        cnt += 1                                # cnt 에 1 추가
        tree(ch1[n])                            # 재귀 호출

    if ch2[n]:                                  # 마찬가치로, ch2[n]도 같은 과정 반복 수행
        cnt += 1
        tree(ch2[n])


for tc in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))

    V = E + 1                                   # 노드는 반드시 간선보다 1개 많다.
    ch1 = [0] * (V + 1)                         # 각 노드에 연결된 왼쪽 자식 노드 확인
    ch2 = [0] * (V + 1)                         # 각 노드에 연결된 오른쪽 자식 노드 확인

    for i in range(0, 2*E, 2):
        if not ch1[arr[i]]:                     # 값이 없으면
            ch1[arr[i]] = arr[i+1]              # 왼쪽 노드 리스트에 해당 값 갱신
        else:                                   # 이미 값이 있다면
            ch2[arr[i]] = arr[i+1]              # 오른쪽 노드 리스트에 해당 값 갱신

    cnt = 1                                     # 자기 자신을 포함시켜야 하므로, 최초 cnt 는 1

    tree(N)                                     # tree 함수 호출

    print(f'#{tc} {cnt}')
