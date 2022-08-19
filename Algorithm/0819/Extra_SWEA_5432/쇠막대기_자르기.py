T = int(input())

for tc in range(1, T+1):
    paren = list(input())
    stack = []
    cnt = [0] * 50000
    for i in range(len(paren)):
        if paren[i] == '(':
            cnt[i] += 1
        elif paren[i] == ')' and paren[i-1] == '(':
            cnt[i] -= 1
            for j in range(i):
                cnt[j] *= 2

    print(f'#{tc} {sum(cnt)}')
