y=int(input("enter the year value:->"))
if ((y%400==0) or (y%100!=0) and (y%4==0)):
    print("Leap year")
else:
    print("not leap year")
    
    
    
    