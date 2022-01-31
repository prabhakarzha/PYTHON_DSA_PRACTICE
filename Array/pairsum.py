def pairsum(A,size,sum):
    A=sorted(A)
    left = 0
    right = size-1
    count=0
    while left < right:
        if (A[left]+A[right] ==sum):
            count+=1
            left+=1
            right-=1
        elif (A[left] + A[right]>sum):
            right-=1
        else:
            left+=1
    if count!=0:
        return count
    else:
       return -1
arr = [8, 7, 2, 5, 3]
# arr=[1,2,3,4,5,6,7]
sum = 8
print(pairsum(arr,len(arr),sum))
            
            
            
            
            
            
            


# def findPair(A, target):
#     for i in range(len(A) - 1):
#         for j in range(i + 1, len(A)):
#             if A[i] + A[j] == target:
#                 print("Pair found", (A[i], A[j]))
#                 return
     
 
 
 
#     print("Pair not found")
# if __name__ == '__main__':
     
#     A = [8, 7, 2, 5, 3, 1]
#     target = 10
 
#     findPair(A, target)