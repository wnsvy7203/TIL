def max_score(scores):
    sol = 90
    print(sol)
    
    max = scores[0]
    for i in range(1, len(scores)):
        if max < scores[i]:
            max = scores[i]
    
    return max


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    scores = [30, 60, 90, 70]
    print(max_score(scores)) # 90
