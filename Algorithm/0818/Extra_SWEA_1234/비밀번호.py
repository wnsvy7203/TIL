for tc in range(1, 11):
    N, S = map(str, input().split())
    stack = []
    for i in S:
        if not stack:                   # 스택이 비어있으면
            stack.append(i)             # 반드시 append

        else:                           # 스택에 값이 있으면
            if i == stack[-1]:          # i와 stack 의 마지막 값을 비교하여 같으면
                stack.pop()             # 빼준다.
            else:                       # 값이 다르면
                stack.append(i)         # 더한다.
    else:
        print(f'#{tc}', end=' ')        # tc 번호 출력
        for i in stack:
            print(i, end='')            # stack 이 리스트이므로, 모든 원소를 따로 출력한다.
        print()
