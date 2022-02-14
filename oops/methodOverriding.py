class Father:
    def Transportation(self):
        print('Cycle')
class Son(Father):
    def Transportation(self):
        print('BIKE')
        
obj=Son()
obj.Transportation()