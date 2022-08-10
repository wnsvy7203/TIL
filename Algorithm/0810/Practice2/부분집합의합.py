T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    n = len(arr)
    sum_0 = False

    for i in range(1, 1 << n):
        sum_arr = 0
        for j in range(n):
            if i & (1 << j):
                sum_arr += arr[j]
        if sum_arr == 0:
            sum_0 = True

    if sum_0 == False:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} 1')