# Which is the Armstrong number?
# Armstrong number is a number that is equal to the sum of cubes of its digits. For example 0, 1, 153, 370, 371 and 407 are the Armstrong numbers.

n = int(input('enter any number:'))
a=list(map(int,str(n)))
b= list(map( lambda x: x**3,a))
if(sum(b)==n):
    print('The number is an armstrong number')
else:
    print("the number isn't armstrong number")
