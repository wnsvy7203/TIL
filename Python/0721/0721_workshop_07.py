def get_strong_word(x1, x2):
    x1_total = 0
    x2_total = 0

    for char in x1:
        x1_total += ord(char)
    
    for char in x2:
        x2_total += ord(char)
    
    if x1_total > x2_total :
        return x1
    elif x1_total < x2_total:
        return x2
    else:
        return x1, x2

print(get_strong_word('delilah', 'dixon'))