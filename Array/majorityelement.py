#(Using Moore’s Voting Algorithm):   



def majorityelement(arr,size):
    ansindex = arr[0]
    count=1
    for i in range(1,size):
        if(arr[i]==arr[ansindex]):
            
            count+=1
        else:
            count-=1
        if count==0:
            ansindex = i
            count = 1
    return arr[ansindex]
arr=[1,1,2,3,1]
print(majorityelement(arr,len(arr))) 
    