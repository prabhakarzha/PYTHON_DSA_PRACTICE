# def largest( arr, n):
#     max = arr[0]
#     for i in range(1,n):
#         if arr[i]>max:

#             max = arr[i]
#     return max

# def maximum(arr,brr,n):
    
    
#     arr=sorted(arr)
#     brr=sorted(brr)
#     return arr[n-1]*brr[0]
# n= int(input("enter no of array:"))
# arr = [int(input("enter first array:")) for i in range(n)]
# brr = [int(input("enter second array:")) for i in range(n)]

# print(maximum(arr,brr,n))


# def maximum(arr,brr,n):
    
    
#     arr=sorted(arr)
#     brr=sorted(brr)
#     return arr[n-1]*brr[0]
# n= int(input("enter no of array:"))
# arr = list(map(int,input("enterfirst array:").split()))
# brr = list(map(int,input("enter second array:").split()))
# print(maximum(arr,brr,n)


def maximum(a):
	max = a[0]
    for i in range(1,len(a)):
	    # if a[i]>max:
        if max<a[i]:
	        max = a[i]
	return max
print(maximum([1,2,3,4,5,6]))



def maximum(a):
    max = a[0]
    for i in range(1,len(a)):
        if max < a[i]:
            max = a[i]
    return max
print(maximum([1,2,,3,5,4,8]))





    
 
 
        
        
        
         
         
         
         
    
     
 
    
     
     
  
 