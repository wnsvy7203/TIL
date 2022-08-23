T = int(input())
for tc in range(1, T+1):
    arr = list(input())
    print(f'#{tc}', end=' ')
    stack = []
    for i in range(len(arr)):
        if arr[i].isdigit():
            print(arr[i], end='')
        else:
            stack.append(arr[i])
    else:
        while stack:
            print(stack.pop(), end='')
    print()
