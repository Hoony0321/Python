class Model:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        print("할머니 area")


    def perimeter(self):
        print(self.width * 2 + self.height * 2)

class Rectangle(Model):
    def __init__(self,length):
        super().__init__(length, length)
    
    def area(self):
        print("부모 area")


class Cube(Rectangle):
    
