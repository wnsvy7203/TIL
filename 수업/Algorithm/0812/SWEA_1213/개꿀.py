for tc in range(1, 11):
    N = int(input())
    a = input()
    b = input()
    cut = b.split(a)
    print(f'#{tc} {len(cut)-1}')