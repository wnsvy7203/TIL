# bronze 2
# 84ms

T = int(input())

for tc in range(1, T+1):
    arr = list(input())
    cnt = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        if arr[i] == 'O':
            cnt[i+1] = cnt[i] + 1

    print(sum(cnt))
