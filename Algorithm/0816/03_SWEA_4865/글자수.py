T = int(input())
for tc in range(1, T+1):
    str1 = str(set(input()))
    str2 = input()

    cnt = [0] * 26 # 알파벳 26자
    for i in range(len(str2)):
        for j in range(len(str1)):
            if str1[j] == str2[i]:
                cnt[ord(str1[j])-65] += 1 # 아스키 코드 활용

    print(f'#{tc} {max(cnt)}')
