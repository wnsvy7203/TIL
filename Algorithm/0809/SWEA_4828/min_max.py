import sys
sys.stdin = open("sample_input.txt")

T = int(input()) # 1 <= T <= 50
for test_case in range(1, T+1):
    N = int(input()) # 5 <= N <= 1000
    arr = list(map(int, input().split()))
    
    maxV = arr[0]
    minV = arr[0]
    for j in range(1, N):
        if maxV < arr[j]:
            maxV = arr[j]
        if minV > arr[j]:
            minV = arr[j]
        
    print(f'#{test_case} {maxV-minV}')
