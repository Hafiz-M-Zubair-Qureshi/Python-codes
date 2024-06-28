# Define a class named Shape and its subclass Square. The Square class has an init function which takes a 
# length as argument.Both classes have a area function which can print the area of the shape where Shape's  
# area is 0 by default.




class Shape:
    shape=0
    def area(self):
        print("Area of shape is=",self.shape)
    class Square:
        def __init__(self,length):
            self.length=length
        def area(self):
            self.shape=self.length**2
            print("Area of shape is=",self.shape)
    
obj=Shape()
Shape.Square(9).area()
