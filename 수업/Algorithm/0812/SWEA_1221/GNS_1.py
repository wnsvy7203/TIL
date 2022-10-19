T = int(input())
for tc in range(1, T+1):
    N = '#' + input()
    arr = list(map(str, input().split()))

    dict_arr = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}

    for i in range(len(arr)):
        for word, num in dict_arr.items():
            if arr[i] == word:
                arr[i] = num

    arr.sort()
    for i in range(len(arr)):
        for word, num in dict_arr.items():
            if arr[i] == num:
                arr[i] = word

    print(f'#{tc}'+'\n', *arr)
