T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    new_arr = sorted(arr)

    # arr과 new_arr을 비교하여,
    # 각각의 인덱스 값의 전후를 비교해
    # 차를 구하면 그 중 최댓값이 답이다.

    sub = [] # 인덱스 값의 차를 받을 빈 리스트 정의
    for i in range(N):
        for j in range(N):
            if arr[i] == new_arr[j]:
                sub.append(j-i)
                break # 찾았으면 반복문을 더 이상 진행하지 않고 다음 인덱스로,

    print(f'#{tc} {max(sub)}') # 최댓값만 출력되도록