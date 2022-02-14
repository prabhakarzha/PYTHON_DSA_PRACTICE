def insertionsort(A):
    n =  len(A)
    for i in range(1,n):
        temp=A[i]
        j=i-1
        while(j>=0 and A[j]>temp):
            A[j+1]=A[j]
            j=j-1
        A[j+1]= temp
            
      
A=[3,5,8,9,6,2]
print('Original Array:',A)
insertionsort(A)
print('Sorted Array:',A)



                
                
                
    
