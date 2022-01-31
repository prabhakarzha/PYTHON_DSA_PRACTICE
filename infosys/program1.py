# value = input('enter a string:')
# total = 0
# for i in value:
#     total = total + 1
# print ('total count of a string=',total)
    
    
        
        



string = input('enter a string:')
lst=[]
for i in string:
    if i not in lst:
        lst.append(i)
for j in lst:
    print(j, '',string.count(j),'times')
    
        


    