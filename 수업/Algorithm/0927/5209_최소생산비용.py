# D3
# 112ms


def backtracking(idx, ans):
    global minV
    if ans >= minV:                                     # ans 가 minV 보다 크거나 같다면
        return                                          # 가지치기

    if idx == N:                                        # 목적지에 도달한다면
        minV = ans                                      # 앞에서 가지치기 하면서 도달했으므로 minV 는 ans
        return

    for k in range(N):
        if not visited[k]:                              # 방문 안 한 경우만 고려하세요
            visited[k] = 1                              # 방문 표시 하시고,
            backtracking(idx + 1, ans + nums[idx][k])   # idx 0 부터 돌아가야지, nums[idx][k] 더해요
            visited[k] = 0                              # 갔다 왔으면 안 가 본 척 하세요


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = [list(map(int, input().split())) for _ in range(N)]
    minV = 100 * N * N                                  # 각 칸의 최댓값은 99에요
    visited = [0] * N                                   # 방문 표시할 리스트요

    backtracking(0, 0)                                  # 인덱스 초깃값은 0, ans 는 초깃값 0

    print(f'#{tc} {minV}')
