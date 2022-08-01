def over(scores):
    cnt = 0
    for i in scores:
        if i >= 60:
            cnt += 1
    
    return cnt
    # 여기에 코드를 작성합니다.


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    scores = [30, 60, 90, 70]
    print(over(scores)) # 3
