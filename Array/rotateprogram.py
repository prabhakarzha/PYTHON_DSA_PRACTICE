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



array = [1,2,3,4,5,6,7,8,9,10]
shift = 4

def printArray(array):
    for i in range(0, len(array)):
        print(array[i], end=' ')

def leftRotation(array, shift):
    for i in range(0, shift):
        temp = array[0]  # saving First element in temp variable
        for j in range(0, len(array) - 1):  # shift remaining array elements one by one
            array[j] = array[j + 1]

        array[len(array) - 1] = temp
    return array

print("Array Before Rotation: ")
printArray(array)

rotatedArray = leftRotation(array, shift)
print("\nArray after left rotation: ")
printArray(rotatedArray)




        