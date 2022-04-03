def firstoccur(A,n,key):
    start = 0
    end = n-1
    result = -1
    while(start<=end):
        mid = (start+end)//2
        if (key==A[mid]):
            result = mid
            end = mid-1
        elif(key<A[mid]):
            end = mid-1
        elif(key>A[mid]):
            start = mid+1
    return result
A= [1,2,3,2,4,4,4,6,7]
found = firstoccur(A,8,4)
print('result:',found)
            
            
    