arr = list(map(int, input().split()))
sum_arr = 0
for i in range(5):
    sum_arr += arr[i]**2
print(sum_arr % 10)
