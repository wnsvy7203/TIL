import sys
sys.stdin = open('test_input.txt', 'r', encoding = "UTF-8")
# 무슨 말인지는 모르겠지만, python3은 ASNI 기준으로 작성된 파일만 읽어온단다.

def BruteForce_cnt(pattern, text):
    cnt = 0
    for i in range(len(text) - len(pattern) + 1):
        for j in range(len(pattern)):
            if text[i+j] != pattern[j]:
                break
        else:
            cnt += 1
    else:
        return cnt

for tc in range(1, 11):
    N = int(input())
    t = input()
    test_case = input()
    print(f'#{tc} {BruteForce_cnt(t, test_case)}')