def calculate_itr(n):
    
    while n>0:
        k=n ** 2
        print(k)
        n = n-1
calculate_itr(4)

def calculate_rec(n):
    
    if n>0:
        k=n ** 2
        print(k)
        calculate_rec(n-1)
calculate_rec(4)


def factorial_rec(n):
    if n == 0:
        return 1
    return factorial_rec(n-1)*n
num = int(input('Enter a Number:'))
print(factorial_rec(num))

def factorial(n):
    f = 1
    for i in range(1,n+1):
        f = f*i
    return f
x =4
result = factorial(x)
print(result)
    


