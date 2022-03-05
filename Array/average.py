n = int(input('enter the number of element to be isert:'))
a= []
for i in range(0,n):
    elem = int(input('enter the element'))
    a.append(elem)
avg = sum(a)/n
print(avg)