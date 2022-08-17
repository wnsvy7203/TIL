a = 0
b = 1
n = 20
for _ in range(1000):
    a, b = b, a+b
print(b)