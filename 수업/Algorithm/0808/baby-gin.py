T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input()))

    cnt = [0] * 10
    for i in range(10):
        for j in arr:
            if i == j:
                cnt[i] += 1

    tri = run = 0
    i = 0
    while i < 10:
        if cnt[i] >= 3:
            cnt[i] -= 3
            tri += 1
            continue
        if cnt[i] >= 1 and cnt[i+1] >= 1 and cnt[i+2] >= 1:
            cnt[i] -= 1
            cnt[i+1] -= 1
            cnt[i+2] -= 1
            run += 1
            continue
        i += 1
    if run + tri == 2:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')