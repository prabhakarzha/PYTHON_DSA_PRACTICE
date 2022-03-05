arr = [1,2,3,4,5,6,7,8]
# k=3

def reverse(arr,start, end):
    while start < end:
        
        
        arr[start],arr[end] = arr[end],arr[start]
        
