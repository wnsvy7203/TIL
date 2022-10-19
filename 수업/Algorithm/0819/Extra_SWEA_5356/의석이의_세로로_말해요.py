T = int(input())

for tc in range(1, T+1):
    arr = [list(input()) for _ in range(5)]
    len_arr = []

    for i in arr:
        len_arr.append(len(i))

    read = ''

    for i in range(5):
        for j in range(len_arr[i]):
            if arr[j][i]:
                read += arr[j][i]

    print(f'#{tc} {read}')
