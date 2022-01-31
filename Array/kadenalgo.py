#find largest sum in subarray



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
arr=[1,1,1]
print(maxsumarray(arr,len(arr)))
        

        
            
            
            
            
            