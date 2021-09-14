def pushzero(arr,n):
    count = 0
    for i in range(n):
        if arr[i]!=0:
            arr[count]=arr[i]
            count+=1
    while count<n:
        arr[count]=0
        count+=1
arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
n = len(arr)
pushzero(arr, n)
print("Array after pushing all zeros to end of array:")
print(arr)


def array(arr,n):
    l1=[]
    l2=[]
    for i in range(n):
        if(arr[i]>0):
            l1.append(arr[i])
        else:
            l2.append(arr[i])
    output=l1+l2
    return output
arr=[1,3,0,4,0,3,0,2,4]
n=len(arr)
print(array(arr,n))