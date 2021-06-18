# Assignment/Task 1 

# Colors = ["Yellow","Green","White","Black"] 
# Fruits=["Apple","Papaya","Mango","Orange"] 
# Animals=["Tiger","Lion","Deer","Zebra"] 

# i. Write a program that asks user to enter a Color/Fruit/Animal name and 
# it should tell which category belongs to , like its is a fruit or color or Animal 

# ii. Write a program that asks user to enter two items and
# it tells you if they both are in same category or not. For example if I enter yellow and Black, 
# it will print "Both are colors" but if I enter yellow and Tiger it should print "They don't belong to same category" 



Colors = ["Yellow","Green","White","Black"] 
Fruits=["Apple","Papaya","Mango","Orange"]  
Animals=["Tiger","Lion","Deer","Zebra"] 
 
 
inp = input("Enter the Color/Fruits/Animal name:")
if inp in Colors:
    print('Color')
elif inp in Fruits:
    print('Fruit')
elif inp in Animals:
    print('Animal')



Colors = ["Yellow","Green","White","Black"] 
Fruits=["Apple","Papaya","Mango","Orange"]  
Animals=["Tiger","Lion","Deer","Zebra"] 

inp, inps= input("Enter two items:").split()

if (inp in Colors and inps in Colors ):
    
    print("Both are colors")
    

elif (inp in Fruits and inps in Fruits): 
    
    print('Both are Fruits') 
elif (inp in Animals and inps in Animals): 
    print('Both are Animals') 
else: 
    print("They don't belong to same category") 

 
 

 
 
 
 
 
 

