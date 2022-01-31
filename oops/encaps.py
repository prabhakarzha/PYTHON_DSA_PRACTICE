
# encapsulation ka mtlb saare method and variable ko private krke ek class k under daalna hota h
#private access ek class s bahar dusre class m access ni kr skta



class Encaps:
    __a=10    #private variable
    def __display(self):  #private method
        print('weclome man')
        print(self.__a)
        # self.__display()  #this will wrong approach
    def Help(self):
        self.__display()
obj=Encaps()
obj.Help()
        