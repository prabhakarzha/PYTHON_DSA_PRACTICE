a =[]
size = int(input('enter the size of an array:-'))
for i in range(size):
    val=int(input('enter no:-'))
    a.append(val)
key=int(input('enter key value which you want to insert:-'))
def listinsert(a,size,key):
    a.append(None)
    i=size-1
    while i>=0 and a[i]>key:
        a[i+1]=a[i]
        i=i-1
    a[i+1]=key
    print('updating list',a)
    
print('original list is:-',a)
listinsert(a,size,key)
        
    
