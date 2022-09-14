for _ in range(1, int(input())+1):
    stack = []
    for i in input():
        if i == '(':                # '('이면 stack에 더한다.
            stack.append(i)
        elif i == ')':              # ')'이면 stack에 원소가 남아있으면
            if stack:               
                stack.pop()         # 빼준다.
            else:
                print(f'#{_} {-1}') # stack에 원소가 없다는 것은 짝이 맞지 않다는 뜻이므로,
                break
    else:                           # for문이 끝났을 때,
        if stack:                   # 원소가 남아있으면 짝이 안 맞으므로
            print(f'#{_} {-1}')
        else:                       # 원소가 없다면 짝이 맞으므로
            print(f'#{_} {1}')