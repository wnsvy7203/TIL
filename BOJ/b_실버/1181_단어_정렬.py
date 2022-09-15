import sys

N = int(sys.stdin.readline())       # 단어 길이 최대 50
word = [sys.stdin.readline().rstrip() for _ in range(N)]

word = list(set(word))

cnt = [[] for _ in range(51)]
for i in word:
    cnt[len(i)].append(i)

for i in range(51):
    if cnt[i]:
        cnt[i].sort()

for i in range(51):
    if cnt[i]:
        for j in range(len(cnt[i])):
            print(cnt[i][j])
