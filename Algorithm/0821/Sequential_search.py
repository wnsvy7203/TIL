def sequentialSearch(a, n, key): # a = 검색할 리스트, n은 원소의 개수, key는 찾는 값
        i = 0
        while i < n and a[i] != key:
            i += 1
        if i < n:
            return i
        else:
            return -1

def sequential_Search(a, n, key):
    while i < n and a[i] < key:
        i += 1
    if i < n and a[i] == key:
        return i
    else:
        return -1