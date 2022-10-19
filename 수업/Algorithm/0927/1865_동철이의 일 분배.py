# D4
# 5878ms

import sys
sys.stdin = open('input.txt')


def backtracking(idx, ans):
    global maxV
    if ans <= maxV / 100:                               # ans 가 maxV / 100 보다 작거나 같다면
        return                                          # 가지치기

    if idx == N:                                        # 목적지에 도달한다면
        maxV = ans * 100                                # 위에서 가지치기 했으므로 maxV 는 ans
        return

    for k in range(N):
        if ratio[idx][k] == 0:
            continue
        if not visited[k]:                              # 방문 안 한 경우만 고려하세요
            visited[k] = 1                              # 방문 표시 하시고,
            backtracking(idx + 1, ans * ratio[idx][k] / 100)  # idx 0 부터 돌아가야지, ratio[idx][k] 곱해요
            visited[k] = 0                              # 갔다 왔으면 안 가 본 척 하세요


T = int(input())

for x in range(1, T+1):
    N = int(input())
    ratio = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    maxV = 0

    backtracking(0, 1)

    print(f'#{x} {maxV:.6f}')
