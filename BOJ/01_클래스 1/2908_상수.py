# Bronze 2
# 68ms

A, B = map(int, input().split())
A = (A % 10)*100 + ((A % 100)-(A % 10)) + (A // 100)
B = (B % 10)*100 + ((B % 100)-(B % 10)) + (B // 100)
print(max(A, B))
