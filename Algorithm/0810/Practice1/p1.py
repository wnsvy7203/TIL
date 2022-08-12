T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    new_arr = [[0] * (N+2) for _ in range(N+2)] # 원소가 모두 0인 (N+2)*(N+2)의 2차원 배열 선언

    for i in range(1, N+1):
        for j in range(1, N+1):
            new_arr[i][j] = arr[i-1][j-1] # arr에 받은 값을 new_arr에 옮긴다.
    
    for i in range(N+2):
        for j in range(N+2):
            if i == 0:
                new_arr[i][j] = new_arr[i+1][j]
            if j == 0:
                new_arr[i][j] = new_arr[i][j+1]
            if i == N+1:
                new_arr[i][j] = new_arr[i-1][j]
            if j == N+1:
                new_arr[i][j] = new_arr[i][j-1]
                
    sum_abs = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            sum_abs += abs(new_arr[i][j] - new_arr[i-1][j])
            sum_abs += abs(new_arr[i][j] - new_arr[i+1][j])
            sum_abs += abs(new_arr[i][j] - new_arr[i][j-1])
            sum_abs += abs(new_arr[i][j] - new_arr[i][j+1])

    print(f'#{tc} {sum_abs}')