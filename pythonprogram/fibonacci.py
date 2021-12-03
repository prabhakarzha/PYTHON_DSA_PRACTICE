# n=int(input("enter any number:"))

# def fib(n):
#     a=0
#     b=1
#     # print(a)
#     # print(b)
#     for i in range(2,n):
#          c=a+b
#          a=b
#          b=c
#          print(c)
# output = fib(n)
# print(output)
    
    
# recursive fibonacci series nth number  
# num = int(input("enter a number:"))
   
# def fib(n):
#     if n==0:
#         return 0
#     elif(n==1):
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
# print(fib(num))    

# iterative fibonacci series nth number
    
num = int(input("enter a number:"))

def fib(n):
    a = 0
    b = 1
    for i in range(1,n-1):
        c=a+b
        a=b
        b=c
        
    return c
print(fib(num))

    
     
         
    
    


  
   
   
   
   

    

