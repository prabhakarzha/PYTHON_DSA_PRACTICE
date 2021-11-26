i=int(input("enter no of candies by customer:"))

n=10
k=5
if(i>n):
    print("Invalid input")
    print("Number of candies available:", end="")
    print(n)
elif(i<=0):
    print("invalid input")
    print("Number of candies available:", end="")
    print(n)
else:
    print("Number of candies sold:",end="")
    print(i)
    print("Number of candies available:",end="")
    print(n-i)









