T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))
    for i in range(N-1, 0, -1): # num을 버블정렬한다.
        for j in range(0, i):
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]

    lst = [0] * 10
    for i in range(10):
        if i % 2 == 0:
            lst[i] = num[N-1-(i//2)]
        else:
            lst[i] = num[i//2]

    print(f'#{tc}')
    for i in range(10):
        print(lst[i], end = ' ')
    print()