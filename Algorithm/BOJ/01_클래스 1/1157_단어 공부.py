# bronze 1
# 324ms

A = input().upper()               # 소문자/대문자 구분 없음

cnt = [0] * 26                    # A ~ Z 전부 받는 리스트

for i in A:                       # i가 A에 있으면
    cnt[ord(i)-ord('A')] += 1     # 아스키코드 활용해서 cnt를 변경해준다.

a = max(cnt)                      # a = cnt 값 중 가장 큰 값
if cnt.count(a) > 1:              # cnt 내에 a가 1개보다 많으면
    print('?')                    # ? 출력
else:                             # cnt 내에 a가 1개면,
    for i in range(26):                 # a의 인덱스 값 출력
        if cnt[i] == a:
            print(chr(i+ord('A')))
