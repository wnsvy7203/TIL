# silver 1
# 36ms

# 분할 정복을 사용할 건데 a, b, c는 2,147,483,647 이하의 자연수
# b가 1이면 그냥 구하면 그만
# b를 짝수 홀수로 나눈다 치면
# a ** 4 = (a ** 2) ** 2
# a ** 5 = ((a ** 2) ** 2) * a

A, B, C = map(int, input().split())


def division(a, b, c):
    if b == 1:
        return a % c

    temp = division(a, b // 2, c)

    if not b % 2:
        return (temp * temp) % c
    else:
        return (temp * temp * a) % c


print(division(A, B, C))
