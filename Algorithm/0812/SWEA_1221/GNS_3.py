T = int(input())
for tc in range(1, T+1):
    N = '#' + input()
    arr = list(map(str, input().split()))

    numbers = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

    for i in range(len(arr)):
        for idx, j in enumerate(numbers):
            if arr[i] == j:
                arr[i] = idx

    arr.sort()

    for i in range(len(arr)):
        for idx, j in enumerate(numbers):
            if arr[i] == idx:
                arr[i] = j

    print(f'#{tc}')
    print(*arr)