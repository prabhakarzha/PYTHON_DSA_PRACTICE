# n = int(input("enter an array"))
# arr=  list(map(int,input().split()))
# s = 0
# c = 0
# for i in range(len(arr)):
#     if arr[i]>=0:
#         s += arr[i]
#         c +=1
        
# if s==0 and c==0:
#     s = max(arr)
#     c = 1
# print(s,c)



# def  even_odd(num):
#     if num%2==0:
#         return "the number {} is even" .format(num)
#     else:
#         "the number {} is odd" .format(num)
# num=[1,2,3,4,5,6,7,8,9,24,56,78]
# print(list(map(even_odd,num)),end="")


li=[1,2,3,4,5,6,7,8,9]
def func(x):
    return x*x
print(list(map(func,li)),end="")
# newList = []
# for x in li:
#     newList.append(func(x))
# print(newList)