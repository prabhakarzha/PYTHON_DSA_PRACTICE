# def binarysearch(A,n,key):
#     l=0
#     r=n-1
#     while l<=r:
#         m = (l+r)//2
#         if key == A[m]:
            
#             return m
        
#         elif key <A[m]:
#             r = m-1
#         elif key > A[m]:
#             l=m+1
#     return -1
# A =[3,5,8,9,12,54,56]
# found =binarysearch(A,6,9)
# print('Result:',found)
        
        

def binarysearch_recursive(A,key,l,r):
    if l>r:
        return -1
    else:
        mid = (l+r)//2
        if key == A[mid]:
            return mid
        elif key < A[mid]:
            return binarysearch_recursive(A,key,l,mid-1)
        elif key > A[mid]:
            return binarysearch_recursive(A,key,mid+1,r)
    
A = [15,21,47,84,96]
result = binarysearch_recursive(A,84,0,4)
print("result:",result)          
    