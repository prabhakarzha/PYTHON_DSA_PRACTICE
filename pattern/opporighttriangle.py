n = int(input('enter number:-'))
for i in range(n):
    
    for j in range(i,n):
        print(' ',end='')
    for j in range(i+1):
        print('*',end='')
    print('\n')
