def func(n):
    if(n==2 or n==3):
        print(n-1)
    res =1
    while(n>4):
        n-=3
        res=res*3
    print(n*res)
n=6
func(n)