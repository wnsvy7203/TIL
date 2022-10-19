import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    queue = list(map(int, input().split()))
    cnt = 0
    while True:
        cnt += 1
        a = queue.pop(0)
        if a-cnt <= 0:
            queue.append(0)
            break
        queue.append(a-cnt)
        if cnt == 5:
            cnt = 0
    print(f'#{tc}', *queue)
