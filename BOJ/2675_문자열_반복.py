T = int(input())

for tc in range(1, T+1):
    R, S = map(str, input().split())

    for i in S:
        for j in range(int(R)):
            print(i, end='')
    print()
