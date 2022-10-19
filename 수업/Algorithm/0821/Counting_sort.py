def Counting_Sort(A, B, k):
    C = [0] * (k+1)
    
    for i in range(len(A)):
        C[A[i]] += 1
    
    for i in range(1, len(C)):
        C[i] += C[i-1]
    
    for i in range(len(B)-1, -1, -1):
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]
    
    return B

A = [0, 1, 2, 3, 4, 0, 1, 3, 2]
B = [0] * 9
k = 9

print(Counting_Sort(A, B, k))