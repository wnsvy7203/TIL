T = int(input())

for _ in range(1, T+1):
    N = int(input())          # N은 10의 배수로 주어지고
    memo = [1, 3]             # memo 의 인덱스 시작점은 0이므로
    n = int((N - 10) / 10)    # 괴리를 해소하기 위한 변수 n 선언

    for i in range(2, n+1):   # memo[0]과 memo[1]이 각각 1, 3으로 정해져있고, 구하고자 하는 값은 memo[n]이므로
        memo.append(memo[i-2]*2 + memo[i-1])
                              # 2번째 전의 값에서 2를 곱하고, 바로 앞의 값을 더한다는 규칙 활용
    print(f'#{_} {memo[-1]}') # 메모의 마지막 값 출력
