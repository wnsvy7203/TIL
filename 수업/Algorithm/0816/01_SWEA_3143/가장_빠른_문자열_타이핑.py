T = int(input())

for tc in range(1, T+1):

    A, B = map(str, input().split()) # 1 <= A <= 10000, 1 <= B <= 100

    # 원래는 전체 길이만큼 타이핑을 해야 하니까 len(A)
    # len(B)*의 길이에 A에 B가 있는 만큼 빼준다.
    # 한 번은 입력해줘야 하니까 한 번은 다시 더 해준다.
    # 즉, (len(B)-1) * A.count(B)
    cnt = len(A) - (len(B)-1) * A.count(B)

    print(f'#{tc} {cnt}')