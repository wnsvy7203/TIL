def enq(n):
    global last
    last += 1       # 마지막 정점 추가
    heap[last] = n  # 마지막 정점에 key 추가

    c = last
    p = c // 2      # 완전 이진트리이므로 부모 정점 번호

    while p and heap[p] < heap[c]:  # 부모가 있고, 부모 < 자식인 경우 자리 교환
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2


def deq():
    global last
    temp = heap[1]          # 루트 백업
    heap[1] = heap[last]    # 삭제할 노드의 키를 루트에 복사
    last -= 1               # 마지막 노드 삭제
    p = 1                   # 루트에 옮긴 값을 자식과 비교
    c = p * 2               # 왼쪽 자식
    while c <= last:        # 자식이 하나라도 있으면
        if c+1 <= last and heap[c] < heap[c+1]:     # 오른쪽 자식도 있고, 오른쪽 자식이 더 크면
            c += 1          # 비교 대상을 오른쪽 자식으로 변경
        if heap[p] < heap[c]:
            heap[p], heap[c] = heap[c], heap[p]
            p = c
            c = p * 2
        else:               # 부모가 더 크면
            break           # 비교 중단
    return temp


heap = [0] * 100
last = 0

enq(2)
enq(5)
enq(7)
enq(3)
enq(4)
enq(6)
while last:
    print(deq())
