class Polygon:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        
        
        
class Rectangle(Polygon):
    def area(self):
        return self.width * self.height

rect = Rectangle(2,4)
print(rect.area())
