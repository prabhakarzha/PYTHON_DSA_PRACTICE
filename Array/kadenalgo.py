#find largest sum contigious subarray



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
print(maxsumarray(arr,len(arr))) # ❤️❤️❤️❤️❤️😂


        

        
            
            
            
            
            