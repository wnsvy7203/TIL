def backtrack(row, n, temp):
    global mini             # 전역 변수 최솟값 mini
    if len(stack) == n:     # stack 의 길이가 n과 같아지면
        if temp < mini:     # 임시 합 temp 가 현재 최솟값 mini 보다 작을 때
            mini = temp     # mini 갱신
        elif mini < temp:   # 가지치기 Pruning: 현재 최솟값 mini 보다 임시합이 커지면 길이와 상관없이 재귀 함수 중단
            return
    else:                   # stack 에 중복을 허용하지 않는 순열 생성
        for i in range(n):
            if i not in stack:
                stack.append(i)
                backtrack(row + 1, n, temp + arr[row][stack[-1]])
                stack.pop()


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    stack = []
    # N일 때 최댓값으로 초기값 설정
    mini = 9 * N
    backtrack(0, N, 0)

    print(f'#{tc} {mini}')

