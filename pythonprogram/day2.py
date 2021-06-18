# 1. Write a python program that can tell you if your grade score good or not . Normal Score range is 40 to 60. 
# i. Ask user to enter his score. 
# ii. If it is below 40 to 60 range then print that score is low 
# iii. If it is above 60 then print that it is good otherwise print that it is normal 


# inp = int(input("Enter Your Score: "))
# if inp<40:
#     print("Score is low")
# elif inp>=40 and inp<=60:
#     print("Score is Normal")
# elif inp>60:
#     print("Score is good")
# else:
#     print("it is normal")
    
    
    
    
    
# 1. After appearing in exam 10 times you got this result, 
# result = ["Pass","Fail","Fail","Pass","Fail","Pass","Pass","Fail","Fail","Fail"] 
# Using for loop figure out how many times you got Pass 

result = ["Pass","Fail","Fail","Pass","Fail","Pass","Pass","Fail","Fail","Fail"] 


c = 0
for i in result:
    
    
    if i == "Fail":
        
        
        c+=1
        
        print(c)






