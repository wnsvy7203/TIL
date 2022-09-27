def backtracking(idx, cnt):
    global result
    if cnt >= result:                        # cnt 가 result 보다 크거나 같다면
        return                               # 어짜피 최솟값이 못되니까 가지치기

    if idx >= N-1:                           # 목적지에 도달한다면
        result = cnt                         # (위에서 가지치기 했으므로) result 는 cnt
        return

    for i in range(1, battery[idx]+1):       # battery 의 idx 번째 배터리 용량만큼
        backtracking(idx + i, cnt + 1)       # 다음칸으로 가면서 탐색


T = int(input())
for tc in range(1, T+1):
    N, *battery = map(int, input().split())
    result = float('inf')

    backtracking(0, -1)                      # 출발지에서는 count 를 안하기 때문에 -1로 시작

    print(f'#{tc} {result}')
