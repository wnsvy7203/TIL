T = int(input())

for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    # 가로
    flag = True
    for i in range(9):
        check = [0] * 9
        result = 1
        for j in range(9):
            check[arr[i][j]-1] = 1
        for k in range(9):
            result *= check[k]
            if result == 0:
                flag = False

    for i in range(9):
        check = [0] * 9
        result = 1
        for j in range(9):
            check[arr[j][i]-1] = 1
        for k in range(9):
            result *= check[k]
            if result == 0:
                flag = False

    for i in range(0, 9, 3):
        check = [0] * 9
        result = 1
        for j in range(3):
            check[arr[i][j]-1] = 1
            check[arr[i+1][j]-1] = 1
            check[arr[i+2][j]-1] = 1
        for k in range(9):
            result *= check[k]
            if result == 0:
                flag = False

    print(f'#{tc} {int(flag)}')
