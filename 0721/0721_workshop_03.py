def dict_list_sum(numbers):
    sum_ages = 0
    for i in numbers:
        sum_ages += i['age']
    return sum_ages

print(dict_list_sum([{'name': 'kim', 'age': 12},
                     {'name': 'lee', 'age': 4}]))