salt = []
water = []
i = 0

while i < 5 :
    i += 1
    s = input(f'{i}. 소금물의 농도(%)와 소금물의 양(g)을 입력하십시오. :')
    if s == 'Done':
        break
    
    S = int(s[0:s.find('%')])
    L = int(s[s.find(' ') + 1 : s.find('g') : 1])

    salt.append(S * L / 100)
    water.append(L)

print('{:.2f}% {}g'.format( sum(salt) / sum(water)  * 100, sum(water)))