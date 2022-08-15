def get_secret_word(numbers):
    word = ''

    for i in numbers:
        word += chr(numbers)
    return word

print(get_secret_word([83, 115, 65, 102, 89]))
