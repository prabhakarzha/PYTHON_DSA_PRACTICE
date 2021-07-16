def binarysearch(A,n,key):
    l=0
    r=n-1
    while l<=r:
        m = (l+r)//2
        if key == A[m]:
            
            return m
        
        elif key <A[m]:
            r = m-1
        elif key > A[m]:
            l=m+1
    return -1
A =[3,5,8,9,12,54,56]
found =binarysearch(A,6,9)
print('Result:',found)
        
        
        
        
    