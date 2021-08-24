# python program for find largest prime factor of a number 
import math
def MaxPrime(n):
    # initialize prime by -1
    prime = -1
    # even number 
    while n%2==0:
        prime=2
        
        n/=2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n%i==0:
            prime = i
            n = n/i
    if n>2:
        prime = n
    return MaxPrime
n = 15
print(MaxPrime(n))


        
        
    