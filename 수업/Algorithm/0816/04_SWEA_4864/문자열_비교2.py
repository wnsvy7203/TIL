T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    cnt = 0
    for i in range(len(str2) - len(str1) + 1):  # BruteForce
        for j in range(len(str1)):
            if str2[i+j] != str1[j]:
                break
        else:
            cnt += 1
            break
    else:
        cnt = 0

    print(f'#{tc} {cnt}')
