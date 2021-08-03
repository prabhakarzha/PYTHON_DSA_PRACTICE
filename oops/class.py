class Car:
    def __init__(self,window,door,enginetype):
        self.window = window
        self.doors = door
        self.enginetype = enginetype
    def self_driving(self):
        return "this is a {} car ".format(self.enginetype)
        
car1= Car(2,5,"engine")

print(car1.self_driving())
# print(car1.window)
