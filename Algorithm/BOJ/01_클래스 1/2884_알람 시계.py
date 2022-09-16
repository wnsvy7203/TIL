# Bronze 3
# 68ms

H, M = map(int, input().split())    # 0 <= H <= 23, 0 <= M <= 59

if 45 <= M <= 59:                   # 45분을 빼도 H가 변하지 않는 경우
    print(H, M-45)
else:                               # 45분을 빼면 H가 변하는 경우
    if H != 0:                      # 0시라면 전날 23시가 되므로,
        print(H-1, M+15)
    else:
        print(H+23, M+15)
