
# input an array and then print the repeating char
arr=[1,2,3,4,2,7,8,8,3]

n=len(arr)
for i in range(0,n):
    
    for j in range(i+1,n):
        
        if arr[i]==arr[j]:
            print (arr[i])