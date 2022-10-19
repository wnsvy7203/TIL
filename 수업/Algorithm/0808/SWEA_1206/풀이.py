import sys

sys.stdin = open('input.txt')

for i in range(10):
    N = int(input())  # N <= 1000
    arr = list(map(int, input().split()))  # 빌딩의 높이는 최대 255
    cnt = 0  # 조망권이 확보된 칸을 세야지

    for j in range(2, N-2):  # 양 끝의 두 칸에는 건물이 지어지지 않는다.
        maxV = arr[i-2]
        if arr[j] > arr[j-2] and arr[j] > arr[j-1] and arr[j] > arr[j+1] and arr[j] > arr[j+2]: # 이게 맞나..?
            for k in range(j - 2, j + 3): # j-2에서 j+2까지 확인
                if k == j: # 확인 불필요
                    continue
                else:
                    if maxV < arr[k]: # 제일 큰 수에서 두 번째 큰 수를 빼면 cnt 값 확인 가능
                        maxV = arr[k]
            cnt += (arr[j] - maxV) # 뺐으면 더해
    print(f'#{i + 1} {cnt}') # i가 0부터니까 1을 더해서 출력한다.