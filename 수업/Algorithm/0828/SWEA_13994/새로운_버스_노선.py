T = int(input())

for tc in range(1, T+1):
    N = int(input())
    info = [list(map(int, input().split())) for _ in range(N)]
    cnt = [0] * 1001

    for i in range(N):
        cnt[info[i][1]] += 1
        cnt[info[i][2]] += 1

        if info[i][0] == 1:
            for j in range(info[i][1]+1, info[i][2]):
                cnt[j] += 1
        elif info[i][0] == 2:
            if info[i][1] % 2:
                for j in range(info[i][1]+1, info[i][2]):
                    if j % 2:
                        cnt[j] += 1
            else:
                for j in range(info[i][1]+1, info[i][2]):
                    if j % 2 == 0:
                        cnt[j] += 1
        else:
            if info[i][1] % 2:
                for j in range(info[i][1]+1, info[i][2]):
                    if j % 3 == 0 and j % 10:
                        cnt[j] += 1
            else:
                for j in range(info[i][1]+1, info[i][2]):
                    if j % 4 == 0:
                        cnt[j] += 1

    print(f'#{tc} {max(cnt)}')
