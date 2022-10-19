import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]    

    maxV = 0 # 최댓값을 담을 변수

    for i in range(100): # 먼저 행의 합부터
        sum_row = 0 # 각 행의 합을 담을 변수
        for j in range(100):
            sum_row += arr[i][j]
        if maxV < sum_row :
            maxV = sum_row
    
    for j in range(100): # 열의 합
        sum_col = 0 # 각 열의 합을 담을 변수
        for i in range(100):
            sum_col += arr[i][j]
        if maxV < sum_col:
            maxV = sum_col

    for i in range(100): # 인덱스가 같은 대각선의 합
        sum_x = 0 # 대각선의 합을 담을 변수
        sum_x += arr[i][i]
        if maxV < sum_x:
            maxV = sum_x
    
    for i in range(100): # 인덱스가 서로 다른 대각선의 합
        sum_y = 0
        sum_y += arr[i][99-i]
        if maxV < sum_y:
            maxV = sum_y
    
    print(f'#{n} {maxV}')