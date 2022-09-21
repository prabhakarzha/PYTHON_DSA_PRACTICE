def equilibrium(arr):
    leftsum = 0
    rightsum = 0
    n=len(arr)
    
    for i in range(n):
        leftsum = 0
        rightsum = 0
        
        for j in range(i):
            leftsum = leftsum + arr[j]
            
        for j in range(i+1,n):
            rightsum = rightsum + arr[j]
            
        if leftsum ==rightsum:
            return i
    return -1

arr = [1,3,5,2,2]
print(equilibrium(arr))
        