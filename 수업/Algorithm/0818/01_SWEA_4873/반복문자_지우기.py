T = int(input())

for _ in range(1, T+1):
    stack = [1]                 # 인덱스 에러 방지
    arr = map(str, input())
    for i in arr:               # arr 안을 돌면서
        if i == stack[-1]:      # stack의 마지막 값과 같으면
            stack.pop()         # 뺀다
        else:                   # 다르면
            stack.append(i)     # 더한다
    else:                       # for 문이 끝났을 때,
        print(f'#{_} {len(stack)-1}')  # 1을 임의로 넣었으므로
