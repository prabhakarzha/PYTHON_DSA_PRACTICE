def primefactor(num):
    temp = num 
    i = 2
    while temp>1:
        if temp %i==0:
            print(i,end=' ')
            temp = int(temp/i)
        else:
            i=i+1
num = int(input("enter any nnumber:-"))

output = primefactor(num)
print(output)
    
    
    