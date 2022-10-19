for tc in range(1, 11):  # 테스트 케이스 10개
    N = int(input())
    arr = [list(input()) for _ in range(100)]

    cnt = []  # 펠린드롬일 경우, 그 길이를 받을 빈 리스트 정의
    # 가로줄 확인
    for i in range(100):
        for j in range(100):
            for k in range(99, j, -1):
                new_arr = []
                if k != 99:
                    if arr[i][j] == arr[i][k]:
                        new_arr = arr[i][j:k+1]
                        if new_arr == new_arr[::-1]:  # 펠린드롬이면
                            cnt.append(len(new_arr))  # 그 길이를 더한다.
                else:
                    if arr[i][j] == arr[i][k]:
                        new_arr = arr[i][j:]
                        if new_arr == new_arr[::-1]:
                            cnt.append(len(new_arr))

    for i in range(100):
        for j in range(i):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]  # arr을 돌린다.

    # 같은 과정 반복 -> 가로줄(원래 세로줄) 확인
    for i in range(100):
        for j in range(100):
            for k in range(99, j, -1):
                new_arr = []
                if k != 99:
                    if arr[i][j] == arr[i][k]:
                        new_arr = arr[i][j:k+1]
                        if new_arr == new_arr[::-1]:
                            cnt.append(len(new_arr))
                else:
                    if arr[i][j] == arr[i][k]:
                        new_arr = arr[i][j:]
                        if new_arr == new_arr[::-1]:
                            cnt.append(len(new_arr))

    if len(cnt) == 0:
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {max(cnt)}')
