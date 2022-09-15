# Bronze 2
# 1436ms


# 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합

# M의 분해합이 N이면, M은 N의 생성자

N = int(input())

made = []
for i in range(1, N):
    n = i
    answer = i
    while n != 0:
        if n % 10:
            answer += (n % 10)
        n = n // 10

    if answer == N:
        made.append(i)

if made:
    print(min(made))
else:
    print(0)
