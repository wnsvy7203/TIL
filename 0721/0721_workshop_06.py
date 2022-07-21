def get_secret_number(word):
    total = 0

    for char in word:
        total += ord(char)
    return total

print(get_secret_number('happy'))
        