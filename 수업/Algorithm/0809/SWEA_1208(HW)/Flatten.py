import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    D = int(input()) # 덤프 횟수(1 <= D <= 1000)
    arr = list(map(int, input().split())) # 상자 높이는 1 이상 100 이하

    for i in range(99, 0, -1):  # 가로의 길이는 항상 100이다.
        for j in range(0, i): # 버블 정렬
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    for i in range(D):
        arr[-1] -= 1 # 제일 큰 거에서 제일 작은 거에 하나를 나눠준다.
        arr[0] += 1
        for j in range(99, 0, -1): # 나눠 줄 때마다 버블 정렬 1번 더
            for k in range(0, j):
                if arr[k] > arr[k+1]:
                    arr[k], arr[k+1] = arr[k+1], arr[k]

    print(f'#{tc} {arr[-1] - arr[0]}')