T = int(input())

for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    for i in range(9):
        sum_arr_c = 0                                                   # 가로줄 확인(모든 가로줄의 합이 45이면 통과)
        for j in range(9):
            sum_arr_c += arr[i][j]
        if sum_arr_c != 45:
            print(f'#{tc} {0}')
            break

        sum_arr_r = 0                                                   # 세로줄 확인(모든 세로줄의 합이 45면 통과)
        for j in range(9):
            sum_arr_r += arr[j][i]
        if sum_arr_r != 45:
            print(f'#{tc} {0}')
            break
    else:                                                               # for 문을 다 통과했을 때,
        for i in range(0, 9, 3):                                        # 0, 3, 6을 시작점으로 하는 윈도우를 설정
            sum_arr_w = 0                                               # window 의 합이 모두 45면 통과
            for j in range(3):
                sum_arr_w += arr[i][j] + arr[i+1][j] + arr[i+2][j]
            if sum_arr_w != 45:
                print(f'#{tc} {0}')
                break
        else:
            print(f'#{tc} {1}')                                         # 모든 for 문을 확인해 통과하면, 1 출력




