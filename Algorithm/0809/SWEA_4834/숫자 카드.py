import sys
sys.stdin = open('sample_input.txt')

T = int(input()) # 1 <= T <= 50
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))

    cnt = [0] * 10 # 각 숫자의 개수를 받을 리스트
    for i in arr:
        for j in range(10):
            if j == i:
                cnt[j] += 1

    max_cnt = 0 # 제일 많은 애
    idx = 0 # 걔 인덱스
    for i in cnt:
        if max_cnt < i:
            max_cnt = i
    for i in range(len(cnt)):
        if cnt[i] == max_cnt:
            idx = i

    print(f'#{tc} {idx} {max_cnt}')