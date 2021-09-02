a=input("enter any string:")
def permutation(a,d,end,j):
    l = len(a)
    for i in range(l):
        d[j]=a[i]
        if j==end:
            print("".join(d))
        else:
            permutation(a,d,end,j+1)

            
def permutations(a):
    l=len(a)
    d=[""]*(l+1)
    a=sorted(a)
    permutation(a,d,l-1,0)
permutations(a)









            