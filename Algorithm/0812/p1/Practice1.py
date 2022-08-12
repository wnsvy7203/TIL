a = 'algorithm'

print(a[::-1]) # 방법 1

b = list(reversed(a)) # 방법 2
b_ = ''.join(b)
print(b_)


c = list(a) # 방법 3
for i in range(len(c) // 2):
    c[i], c[len(a)-1 - i] = c[len(a)-1 - i], c[i]
a = ''.join(c)
print(a)

s = 'algorithm'
for i in range(len(s)): # 방법 4
    print(s[len(s) - 1 - i], end='')
print()

reverse_s = ''
for i in range(len(s)-1, -1, -1): # 방법 5
    reverse_s = reverse_s + s[i]
print(reverse_s)