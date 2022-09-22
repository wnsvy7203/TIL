from itertools import permutations


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    hi = list(range(N))

    res_list = []
    for idx in permutations(hi, N):
        i = 0
        j = 0
        res = 0
        while True:
            if idx[0] == 0 or idx[N-1] != 0:
                break

            res += arr[i][idx[j]]
            i = idx[j]
            j += 1

            if j == N:
                res_list.append(res)
                break

    print(f'#{tc} {min(res_list)}')
