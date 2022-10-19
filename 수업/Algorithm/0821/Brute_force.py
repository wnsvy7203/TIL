def BruteForce_for(pattern, text):
    for i in range(len(text) - len(pattern) + 1):
        # pattern의 처음부터 텍스트 문자열과 비교
        for j in range(len(pattern)):
            if text[i+j] != pattern[j]:
                break
        else:
            return i
    else:
        return -1