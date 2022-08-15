def all_list_sum(numbers):
    result = 0
    for i in numbers:
        for j in range(len(i)):
            result += i[j]
    return result

print(all_list_sum([[1],[2, 3],[4, 5, 6],[7, 8, 9, 10]]))