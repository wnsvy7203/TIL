# bronze 2
# 72ms

arr = list(map(int, input().split()))

if arr[0] == 1:
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]+1:
            print('mixed')
            break
    else:
        print('ascending')
elif arr[0] == 8:
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]-1:
            print('mixed')
            break
    else:
        print('descending')
else:
    print('mixed')
