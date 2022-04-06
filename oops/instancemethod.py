class Employee:
    company ="youtube"
    
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    def get_email(self):  #this is the instance method . which takes self keyword as a first argument
        return f'{self.first_name}{self.last_name}@{Employee.company}.com'

emp1 = Employee('sonu','kashyap')
print(emp1.get_email())