T = int(input())
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for tc in range(1, T+1):
    N, K = map(int, input().split())
    l = len(A)
    cnt = 0 # 부분집합의 합이 K인 부분집합의 개수를 받을 변수 초기화

    for i in range(1 << l):
        arr = []
        sum_K = 0 # 각 부분집합의 합을 받을 변수 초기화
        for j in range(l):
            if i & (1 << j):
                arr.append(A[j])
        if len(arr) == N:
            for j in range(N):
                sum_K += arr[j]
            if sum_K == K:
                cnt += 1

    print(f'#{tc} {cnt}')