class Rectangle():

    def __init__(self, l, w):
        self.l = l
        self.w = w
        
    def Rectangle_Area(self):
        return self.l * self.w
    
l = int(input("Enter the length of a Rectangle"))
w = int(input("Enter the width of a Rectangle"))

NewRectangle = Rectangle(l, w)
print(f"the area of the rectangle is {NewRectangle.Rectangle_Area()}")