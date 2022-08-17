T = int(input())
for tc in range(1, T+1):
    memo = [[1], [1, 1]]
    N = int(input())
    print(f'#{tc}')

    for i in range(2, N):       # memo의 길이가 이미 2이므로 0, 1은 의미가 없다.
        pascal = [1]

        for j in range(i-1):    # 바로 전 줄의 j인덱스의 j+1 인덱스의 값을 더한 후 pascal에 더 해준다.
            pascal.append(memo[i-1][j] + memo[i-1][j+1]) 
        pascal.append(1)        # 맨 뒤에도 1을 더 해줘야 하니까
        memo.append(pascal)    
    
    for i in range(N):
        print(*memo[i])