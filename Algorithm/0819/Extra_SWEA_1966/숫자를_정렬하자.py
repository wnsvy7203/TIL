T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr2 = sorted(arr)
    print(f'#{tc}', *arr2)
