T = int(input())
for tc in range(1, T+1):
    N = '#' + input()
    arr = list(map(str, input().split()))

    numbers = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    new = []

    for i in range(len(numbers)):
        for j in range(len(arr)):
            if arr[j] == numbers[i]:
                new.append(arr[j])

    print(f'#{tc+1} ', end='')
    print(*new)