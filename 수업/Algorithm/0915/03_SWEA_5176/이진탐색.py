# 160ms

T = int(input())


def inorder(n):
    global cnt                      # 전역 변수 cnt 호출
    if n:                           # n 이 0이 아니면
        inorder(ch1[n])             # 중위순회
        numbers[n] = cnt            # 왼쪽에 자식이 없으면, numbers 의 n 번째 인덱스를 cnt로 갱신하고
        cnt += 1                    # cnt 값은 1 더해준다.
        inorder(ch2[n])


for tc in range(1, T+1):
    N = int(input())

    ch1 = [0] * (N+1)               # 왼쪽 자식 노드 확인
    ch2 = [0] * (N+1)               # 오른쪽 자식 노드 확인

    for i in range(1, (N//2)+1):
        ch1[i] = i * 2              # 완전 이진 트리의 특성상 왼쪽은 반드시 존재
        if i * 2 + 1 <= N:
            ch2[i] = i * 2 + 1

    cnt = 1                         # 최초의 cnt 는 1
    numbers = [0] * (N+1)           # 중위순회하면서 값을 갱신할 번호의 리스트 numbers
    inorder(1)                      # 사실상 중위순회

    print(f'#{tc} {numbers[1]} {numbers[N//2]}')
