def inorder(n):
    if n <= N:
        inorder(n*2)
        print(char[n], end='')
        inorder(n*2+1)


for tc in range(1, 11):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    char = [0] * (N + 1)

    for i in range(1, N+1):
        char[i] = arr[i-1][1]

    print(f'#{tc}', end=' ')
    inorder(1)
    print()
