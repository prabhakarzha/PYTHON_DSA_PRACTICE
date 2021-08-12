def reverse(num):
    
    
    rev= 0
    sign=1
    if num<0:
        
        sign=-1
        
        num=num*-1
        
    while(num>0):
        
            
    
    
        rev=(rev*10)+num%10
        
            
        num=num//10
            
    if not -2147483648<rev<2147483647:
        
                
        return 0
           

    return sign*rev


    


print(reverse(-123)) 