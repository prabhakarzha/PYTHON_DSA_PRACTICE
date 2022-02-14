arr=[9,6,7,4,2,1]
def subArray(arr,s):
    result = []
    for x in range(len(arr)):
        result.append(arr[x])
        while(sum(result)>s):
            result.pop(0)
        if(sum(result)==s):
            return result
    return []
print(subArray(arr,10))
        
            
            
            
                
        
    
  

    