try:
    a=int(input("enter the fist number:"))
    b=int(input("enter the second number:"))
    c = a/b
    d=a*b
    e=a+b
    print(c)
    print(d)
    print(e)

except NameError:
    print("user have not define dthe variable")
    
except ZeroDivisionError:
    print("please provide a number gteater than zero")
except TypeError:
    print("try to make the datatype simillar")
except Exception as ex:
    print(ex)
    