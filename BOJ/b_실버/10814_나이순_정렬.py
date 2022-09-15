N = int(input())
arr = [list(map(str, input().split())) for _ in range(N)]

# 나이는 1살에서 200살까지,
# 이름은 알파벳 대소문자, 길이가 100보다 작거나 같은 문자열
# 입력은 가입한 순서대로 주어진다.
cnt = [[] for _ in range(201)]

for i in range(N):
    cnt[int(arr[i][0])].append([arr[i][0], arr[i][1]])

for i in range(201):
    if cnt[i]:
        for j in range(len(cnt[i])):
            print(*cnt[i][j])
