# 1 2 3 4 
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4
# n=5
# for row in range(n):
#     for col in range(row+1):
#         print('*  ',end='')
#     print('\n')
    


# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print('*',end='')
#         j=j+1
#     print('\n')
#     i=i+1

n=int(input('enter the value:-'))
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
print(fact(n))

    
    
    
    