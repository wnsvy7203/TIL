# 137ms

T = int(input())

for tc in range(1, T+1):
    N = float(input())
    string = ''
    flag = True
    n = N
    cnt = 0
    while cnt < 13 and n != int(n):
        cnt += 1
        n *= 2
        if n > 1:
            string += str(int(n))
            n -= 1
        else:
            string += str(int(n))

        if cnt == 13:
            flag = False
            break

    if flag:
        print(f'#{tc} {string}')
    else:
        print(f"#{tc} {'overflow'}")