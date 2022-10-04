# 1부터 12까지의 숫자를 원소로 가진 집합 A가 있다.
# 집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수를 출력하는 프로그램을 작성하시오.
# 해당하는 부분집합이 없는 경우 0을 출력한다.모든 부분 집합을 만들어 답을 찾아도 된다.

# 예를 들어 N = 3, K = 6 경우, 부분집합은 {1, 2, 3}의 경우 1 가지가 존재한다.

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

N, K = map(int, input().split())
n = len(A)
cnt = 0         # 부분집합의 합이 K인 부분집합의 개수를 받을 변수 초기화

for i in range(1 << n):
    arr = []
    sum_K = 0   # 각 부분집합의 합을 받을 변수 초기화
    for j in range(n):
        if i & (1 << j):
            arr.append(A[j])
    if len(arr) == N:
        for j in range(N):
            sum_K += arr[j]
        if sum_K == K:
            print(*arr)
