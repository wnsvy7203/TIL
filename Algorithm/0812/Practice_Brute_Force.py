p = 'is'
t = 'This is a book~!'

def BruteForce(pattern, text):
    i = 0
    j = 0
    while j < len(pattern) and i < len(text):
        if text[i] != pattern[j]:
            i -= j
            j = -1
        i += 1
        j += 1
    if j == len(pattern):
        return i - len(pattern)
    else:
        return -1

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

print(BruteForce(p, t))
print(BruteForce_for(p, t))