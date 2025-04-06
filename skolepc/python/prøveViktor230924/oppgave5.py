A = [4,7,4,1,9,15,6]
B = [5,3,8,13,4]

for i in range(len(B)):
    A.append(B[i])

for i in range(len(A)):
    for j in range(i,len(A)):
        if A[j] < A[i]:
            buffer = A[i]
            A[i] = A[j]
            A[j] = buffer
print(A)