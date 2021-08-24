# Python program to rotate an array by d elements

# 1. declare and initialize an array and n
# 2. save first element of array in temp variable
# 3. shift remaining array elements one by one towards left
# 4. copy temp value to last element in StacksArray
# 5. repeat step 2 to 4 until codition satifies


# array = [1,2,3,4,5]
# shift = 2

# for i in range(0,shift):
#     temp=array[0]
#     for j in range(0,len(array)-1):
#         array[j] = array[j+1]
#     array[len(array)-1] = temp
# for i in range(0,len(array)):
#     print(array[i])



# array = [1,2,3,4,5,6,7,8,9,10]
# shift = 4

# def printArray(array):
#     for i in range(0, len(array)):
#         print(array[i], end=' ')

# def leftRotation(array, shift):
#     for i in range(0, shift):
#         temp = array[0]  # saving First element in temp variable
#         for j in range(0, len(array) - 1):  # shift remaining array elements one by one
#             array[j] = array[j + 1]

#         array[len(array) - 1] = temp
#     return array

# print("Array Before Rotation: ")
# printArray(array)

# rotatedArray = leftRotation(array, shift)
# print("\nArray after left rotation: ")
# printArray(rotatedArray)




# arr = [1,2,3,4,5]
# n = 3
# print("original array: ")
# for i in range(0,len(arr)):
#     print(arr[i],end = " ")
    
    
# for i in range(0,n):
#     last = arr[len(arr)-1];
    
#     for j in range(len(arr)-1,-1,-1):
#         arr[j]= arr[j-1];
#     arr[0] = last;
# print()

# print("Array After Rotation: ")
# for i in range(0,len(arr)):
#     print(arr[i],end=" ")
    
    





        