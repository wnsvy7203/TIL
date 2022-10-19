# 중위표기법으로 주어진 입력값을 후위표기법으로 변형하고,
# 계산

for tc in range(1, 11):
    N = int(input())
    infix = list(input())                                           # 중위표기법으로 주어진 입력값
    infix_stack = []                                                # 연산자를 담을 infix_stack
    postfix = []                                                    # 후위표기법으로 변형된 입력값

    for i in infix:                                                 # infix 의 길이 만큼 반복
        if i.isdigit():                                             # infix 값이 숫자면
            postfix.append(i)                                       # postfix 에 더한다.
        elif i == '+':                                              # infix 값이 +일 때,
            if not infix_stack:                                     # infix_stack 에 연산자가 없다면,
                infix_stack.append(i)                               # 해당 연산자를 추가한다.
            elif infix_stack[-1] == '+':                            # +가 있다면,
                postfix.append(infix_stack.pop())                   # 이미 존재하던 +는 postfix 에 옮기고
                infix_stack.append(i)                               # 해당 연산자를 다시 infix_stack 에 추가한다.
            elif infix_stack[-1] == '*':                            # infix_stack 에 연산자가 '*'가 있다면,
                if len(infix_stack) == 1:                           # 모든 연산자를 모두 infix_stack 에 옮긴 후 추가
                    postfix.append(infix_stack.pop())
                    infix_stack.append(i)
                else:
                    postfix.append(infix_stack.pop())
                    postfix.append(infix_stack.pop())
                    infix_stack.append(i)
        elif i == '*':                                              # infix 값이 * 이라면,
            if (not infix_stack) or (infix_stack[-1] == '+'):       # infix_stack 이 비었거나, +만 있다면
                infix_stack.append(i)                               # infix_stack 에 추가한다.
            else:                                                   # infix_stack 의 마지막 값이 *이라면,
                postfix.append(infix_stack.pop())                   # 이미 존재하던 *는 postfix 에 옮기고
                infix_stack.append(i)                               # 해당 연산자를 다시 infix_stack 에 추가한다.
    else:                                                           # for 문을 모두 반복한 이후,
        while infix_stack:                                          # infix_stack 에 남아있는 모든 연산자를
            postfix.append(infix_stack.pop())                       # postfix 에 옮긴다.

    calculate = []                                                  # 계산
    for i in postfix:                                               # postfix 를 확인해서
        if i.isdigit():                                             # 숫자면
            calculate.append(i)                                     # 리스트에 추가하고
        elif i == '+':                                              # + 일 때 연산
            a = calculate.pop()
            b = calculate.pop()
            calculate.append(int(a) + int(b))
        elif i == '*':                                              # * 일 때 연산
            a = calculate.pop()
            b = calculate.pop()
            calculate.append(int(a)*int(b))
    print(f'#{tc}', *calculate)
