def bubblesort(A):
    n =  len(A)
    for i in range(0,n):
        for j in range(0,n-i-1):
            if A[j]> A[j+1]:
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp
A=[3,5,8,9,6,2]
print('Original Array:',A)
bubblesort(A)
print('Sorted Array:',A)


                
                
                
    
