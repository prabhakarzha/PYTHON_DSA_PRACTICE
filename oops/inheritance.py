class Car:
    def __init__(self,window,door,enginetype):
        self.window = window
        self.doors = door
        self.enginetype = enginetype
    def drive(self):
        print("The Person drive the car")
        
    def fastdrive(self):
        print("maximum speed should be 40km/h")
car=Car(4,5,"diesel")


class audi(Car):
    def __init__(self,window,door,enginetype,enableai):
        super().__init__(window,door,enginetype)
        self.enableai=enableai
    def selfdriving(self):
        print("Audi supports self driving")
audiQ7 = audi(4,5,"diesel",True)
print(audiQ7.fastdrive())
print(audiQ7.selfdriving())





        