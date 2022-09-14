def postorder(n):
    global stack, arr
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        stack.append(arr[n-1][1])


for tc in range(1, 11):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    ch1 = [0] * (N + 1)
    ch2 = [0] * (N + 1)

    for i in arr:
        p = int(i[0])
        if len(i) == 4:
            ch1[p] = int(i[2])
            ch2[p] = int(i[3])

    stack = []
    postorder(1)

    calc = []
    for i in stack:
        if i.isdigit():
            calc.append(int(i))
        else:
            b = calc.pop()
            a = calc.pop()

            if i == '+':
                calc.append(a+b)
            elif i == '-':
                calc.append(a-b)
            elif i == '*':
                calc.append(a*b)
            elif i == '/':
                calc.append(int(a/b))

    print(f'#{tc} {calc[-1]}')
