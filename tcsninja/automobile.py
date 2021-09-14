v=int(input("value of vechile:"))
w=int(input("value of whele:"))
if(w&1)==1 or w<2 or w<=v:
    print("Invalid input")
else:
    x=((4*v)-w)//2
    print("TW={} FW={}".format(x,v-x))

    
