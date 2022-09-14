import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    day, month, quarter, year = map(int, input().split())      # 이용권 가격
    plan = [0] + list(map(int, input().split()))               # 12개월 이용 계획
    price = [0] * 13                                           # 1달치 이용 최소 가격

    for i in range(1, 13):
        price[i] = min(day * plan[i], month) + price[i-1]

        if i > 2:
            price[i] = min(price[i], quarter + price[i-3])

    result = min(price[12], year)

    print(f'#{tc} {result}')

