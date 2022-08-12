def atoi(s):
    i = 0
    for x in s:
        i = i * 10 + ord(x)- ord('0')
    return i

s = '123'
a = atoi(s)
print(a)