def maxsumarray(arr,size):
    maxsum=0
    cursum=0
    for i in range(0,size):
        cursum = cursum+arr[i]
        if (cursum>maxsum):
            maxsum = cursum
        elif (cursum<0):
            cursum =0
    return maxsum
arr=[5,-4,-2,6,-1]
print(maxsumarray(arr,len(arr)))
        
        
# def maxSubArraySum(arr,size):
    
#     cursum = arr[0]
#     maxsum = 0
    
#     for i in range(0, size):
#         maxsum = maxsum + arr[i]
#         if maxsum < 0:
#             maxsum = 0
        
        
#         elif (cursum < maxsum):
#             cursum = maxsum
            
#     return cursum

# arr = [-2, -3, 4, -1, -2, 5, -3]
# print("Maximum Sub Array Sum Is" , maxSubArraySum(arr,len(arr)))
        
            
            
            
            
            