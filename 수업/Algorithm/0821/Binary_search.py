def binarySearch(a, N, key):
    start = 0
    end = N - 1
    while start <= end:
        middle = (start + end) // 2
        if a[middle] == key: # 검색 성공
            return True
        elif a[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return False # 검색 실패

def binarySearch2(a, low, high, key): # 재귀함수 활용 버전
    if low > high: # 검색 실패
        return False
    else:
        middle = (low + high) // 2
        if key == a[middle]: # 검색 성공
            return True
        elif key < a[middle]:
            return binarySearch2(a, low, middle-1, key)
        elif key > a[middle]:
            return binarySearch2(a, middle+1, high, key)