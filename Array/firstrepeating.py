# def findDuplicates(arr, Len):
     
#     ifPresent = False
 
#     # ArrayList to store the output
#     a1 = []
#     for i in range(Len - 1):
#         for j in range(i + 1, Len):
 
#             # Checking if element is
#             # present in the ArrayList
#             # or not if present then break
#             if (arr[i] == arr[j]):
#                 if arr[i] in a1:
#                     break
                 
               
#                 else:
#                     a1.append(arr[i])
#                     ifPresent = True
 
#     # If duplicates is present
#     # then print ArrayList
#     if (ifPresent):
#         print(a1, end = " ")
#     else:
#         print("No duplicates present in arrays")
 
# # Driver Code
# arr = [1,2,3,4,3,5,6,7]
# n = len(arr)
 
# findDuplicates(arr, n)





#Initialize array   
arr = [1, 2, 3, 4,  7, 8, 3];   
   
print("Duplicate elements in given array: ");  
#Searches for duplicate element  
for i in range(0, len(arr)):  
    for j in range(i+1, len(arr)):  
        if(arr[i] == arr[j]):  
            print(arr[j]);  