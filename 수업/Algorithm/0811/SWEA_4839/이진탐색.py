T = int(input()) # 1 <= T <= 50

for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    # 전체 쪽수 P
    # A가 찾을 쪽 번호 Pa
    # B가 찾을 쪽 번호 Pb (1 <= P, Pa, Pb <= 1000)

    s = 1 # 시작점
    e = P # 마지막 페이지

    # A의 경우를 먼저
    cntA = 0
    cntB = 0
    while s <= e:
        cntA += 1
        m = (s + e) // 2
        if Pa == m:
            a = cntA
            s = 1
            e = P
            break
        elif Pa > m:
            s = m
        else:
            e = m
    # 다음은 B
    while s <= e:
        cntB += 1
        m = (s + e) // 2
        if Pb == m:
            b = cntB
            s = 1
            e = P
            break
        elif Pb > m:
            s = m
        else:
            e = m

    # print
    if a < b:
        print(f'#{tc} A')
    elif a > b:
        print(f'#{tc} B')
    else:
        print(f'#{tc} 0')