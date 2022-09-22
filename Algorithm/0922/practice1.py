def selection_sort(arr, s):
    n = len(arr)
    if s == n-1:
        return
    mn = s
    for i in range(s, n):
        if arr[mn] > arr[i]:
            mn = i
    arr[s], arr[mn] = arr[mn], arr[s]

    selection_sort(arr, s+1)


A = [2, 4, 6, 1, 9, 8, 7, 0]
selection_sort(A, 0)
print(A)
