def linearsearch(A,n,key):
    index = 0
    while  index< n:
        if A[index]==key:
            return index
        index =index+1
    return -1
A =[23,45,34,56,21,22]
found =linearsearch(A,6,21)
print('Result:',found)
        
        
def linearsearch(A,n,key):
    index = 0
    while index< n:
        if A[index]==key:
            
            return index
        index = index+1
    return -1   
A =[23,45,34,56,21,22]
found =linearsearch(A,6,21)
print('Result:',found)