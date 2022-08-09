import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1, T+1):
    K, N, M = map(int, input().split())
    # K: 1회 충전으로 이동할 정류장 수
    # N: N번까지 이동
    # M: 충전기가 설치된 정류장 개수
    center = list(map(int, input().split())) # 충전기 위치

    arr = [0] * (N+1) # 정류장을 나타내면
    # bus = 0 # 현재 버스 위치
    # cnt = 0 # 충전 횟수
    for i in center:
        for j in range(N+1):
            if j == i:
                arr[j] == 1

print(arr)




    # print(f'#{test_case} ')
