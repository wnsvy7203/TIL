string = '1DB176C588D26EC'
num = int(string, 16)
output = ''
for i in range(len(string) * 4 - 1, -1, -1):
    output += '1' if num & (1 << i) else '0'

print(output)
