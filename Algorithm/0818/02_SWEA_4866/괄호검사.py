T = int(input())

for tc in range(1, T+1):
    stack = []
    arr = input()
    cnt = 0

    for i in arr:
        if i == '(' or i == '{':        # '('이거나 '{'이면 더한다.
            stack.append(i)

        if i == ')':                    # ')'인 경우
            if stack:                   # 값이 있으면 확인
                if stack[-1] == '(':    # 마지막 값이 '('이면
                    stack.pop()         # 빼고
                else:                   # 아니면
                    break               # 탈출
            else:                       # 애초에 stack이 비었으면 또 탈출
                break

        if i == '}':                    # '}'인 경우에도 ')'일 때와 마찬가지로
            if stack:
                if stack[-1] == '{':
                    stack.pop()
                else:
                    break
            else:
                break

    else:
        if not stack:                   # 모든 과정을 반복했을 때, stack이 비었으면
            cnt = 1                     # 1

    print(f'#{tc} {cnt}')
