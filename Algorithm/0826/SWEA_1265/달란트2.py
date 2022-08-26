for tc in range(1, int(input())+1):
    N, P = map(int, input().split())
    print(f'#{tc} {((N // P)**(P - (N % P)))*(((N // P) + 1)**(N % P))}')
