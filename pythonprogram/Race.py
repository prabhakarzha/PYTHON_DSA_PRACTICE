# 1. Lets say you are running a 50 km race. Write a program that,
# Upon completing each 10 km asks you "are you tired?" If you reply "yes" then it should break
# and print "you didn't finish the race" If you reply "no" then it should continue and ask "are you
# tired" on every km If you finish all 50 km then it should print congratulations message




i=0

# while i!=50:
    
    
    if i ==10:
        
        
        ans=input('Are you tired=')
        
        
        if ans=='yes':
            
            
            print("you didn't finish the race")
            
            
            break
        
        
        elif i>10:
            
            
            ans=input('Are you tired=')
            
            
            if ans=='no':
                
                
                print("you didn't finish the race")
                
                
                break
            
            
            
            i+=1
            
            
             
            if i==50:
                
                 
                
                
                print('Congratulation')
