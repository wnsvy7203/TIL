# Bronze 1
# 72ms

while True:
    arr = list(map(int, input()))

    if len(arr) == 1 and arr[-1] == 0:
        break
    elif arr:
        for i in range(len(arr)//2):
            if len(arr) % 2:
                if arr[len(arr)//2-(i+1)] != arr[len(arr)//2+(i+1)]:
                    print('no')
                    break
            else:
                if arr[len(arr)//2-1-i] != arr[len(arr)//2+i]:
                    print('no')
                    break
        else:
            print('yes')
    else:
        break


