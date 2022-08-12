def strlen(a):
    cnt = 0
    i = 0
    while True:
        if a[i] != '\0':
            i += 1
            cnt += 1
        else:
            break
    return cnt

a = ['a', 'b', 'c', '\0']
print(strlen(a))