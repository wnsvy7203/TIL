import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split()) # 10 <= N <= 100, 2 <= M < N
    arr = list(map(int, input().split())) # 정수 a <= 10000

    maxV = 0
    minV = (10005 * 100)
    for i in range(N-M+1):
        result = 0
        for j in range(M):
            result += arr[i+j]
        if maxV < result:
            maxV = result
        if minV > result:
            minV = result

    print(f'#{test_case} {maxV-minV}')