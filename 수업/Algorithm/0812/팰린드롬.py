a = input()
pellindrom = False
for i in range(len(a) // 2):
    if a[i] == a[len(a)-1-i]:
        pellindrom = True
    else:
        pellindrom = False

print(pellindrom)