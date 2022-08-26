# 1은 켜짐, 0은 꺼짐
# 1 이상, 스위치 개수 이하인 자연수 부여
# 남: if 스위치 번호 == 자기가 받은 수의 배수: 상태를 바꾼다.
# 여: 자기가 받은 수와 같은 번호의 스위치를 중심으로 좌우 대칭 스위치 상태 변경(항상 홀수)
# 스위치의 상태를 1번 스위치에서 시작하여 마지막 스위치까지 한 줄에 20개씩 출력한다.
# 예를 들어 21번 스위치가 있다면 이 스위치의 상태는 둘째 줄 맨 앞에 출력한다.
# 켜진 스위치는 1, 꺼진 스위치는 0으로 표시하고, 스위치 상태 사이에 빈칸을 하나씩 둔다.

N = int(input())                        # 스위치 개수
arr = [-1] + list(map(int, input().split()))   # 스위치 현재 상태
stu = int(input())                      # 학생 수
for _ in range(stu):
    g, n = map(int, input().split())    # 성별, 받은 숫자

    if g == 1:
        for i in range(1, N+1):
            if i % n == 0:
                arr[i] = 1 - arr[i]
    else:
        arr[n] = 1 - arr[n]
        for i in range(N//2):
            if 1 > n-i or n+i > N:
                break
            if arr[n+i] == arr[n-i]:
                arr[n+i] = 1 - arr[n+i]
                arr[n-i] = 1 - arr[n-i]
            else:
                break

for i in range(1, N+1):
    print(arr[i], end=' ')
    if i % 20 == 0:
        print()
