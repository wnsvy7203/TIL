# bronze 2
# 72ms

L = int(input())

string = list(input())
r = 31
M = 1234567891
H = 0
for i in range(L):
    H += (ord(string[i])-96) * (r ** i)

print(H % M)
