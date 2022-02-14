# def product(a,b):
#     p=a*b
#     print(p)
# def product(a,b,c):
#     p=a*b*c
#     print(p)
# # product(2,4)
# product(1,2,3)


class Methhodoverload:
    def display(self,a=None,b=None): #None is default argument
        print(a,b)
obj = Methhodoverload()
obj.display()
obj.display(10)
obj.display(10,20)
