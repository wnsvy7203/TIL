# 235ms


def postorder(n):
    global stack, arr
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        stack.append(arr[n-1][1])


for tc in range(1, 11):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    ch1 = [0] * (N + 1)             # 왼쪽 자식 노드 확인
    ch2 = [0] * (N + 1)             # 오른쪽 자식 노드 확인

    for i in arr:
        p = int(i[0])
        if len(i) == 4:             # 각 트리의 루트는 반드시 연산자이므로, 길이는 4가 아니라면 2이다.
            ch1[p] = int(i[2])
            ch2[p] = int(i[3])

    stack = []                      # 모든 원소를 담을 stack 선언
    postorder(1)                    # 후위 순회(후위표기법?) 호출

    calc = []                       # 계산만 수행할 calc 선언
    for i in stack:                 # 이후는 후위표기법 계산식과 같다.
        if i.isdigit():             # 숫자이면
            calc.append(int(i))     # calc 에 추가하고
        else:                       # 수가 반드시 2개이므로
            b = calc.pop()
            a = calc.pop()

            if i == '+':            # 덧셈 수행
                calc.append(a+b)
            elif i == '-':          # 뺄셈 수행
                calc.append(a-b)
            elif i == '*':          # 곱셈 수행
                calc.append(a*b)
            elif i == '/':          # 나눗셈 수행
                calc.append(int(a/b))

    print(f'#{tc} {calc[-1]}')      # 연산 종료 후 마지막 원소 출력
