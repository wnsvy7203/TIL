# import sys
# sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    area = [[0]*10 for _ in range(10)]

    for i in range(N):
        for j in range(arr[i][0], arr[i][2]+1):
            for k in range(arr[i][1], arr[i][3]+1):
                area[j][k] += arr[i][4]

    cnt = 0
    for i in range(10):
        for j in range(10):
            if area[i][j] == 3:
                cnt += 1

    print(f'#{tc} {cnt}')