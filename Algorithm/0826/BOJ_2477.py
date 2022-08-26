

K = int(input())

Width = {}
Height = []
for _ in range(6):
    D, L = map(int, input().split())
    if D == 1 or D == 2:
        Width.append(L)
    else:
        Height.append(L)

print(max(Width) * max(Height))