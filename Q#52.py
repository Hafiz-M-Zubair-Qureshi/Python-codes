# Define a class named Circle which can be constructed by a radius. The Circle class has a method 
# which can compute the area.


import math

class Circle:               # create class
    def __init__(self,radius):
        self.radius=radius
    def area(self):                       # create method for calculate the radius
        return math.pi * (self.radius**2)     # return the value of radius

x=Circle(7)                   # give the value of radius
print(x.area())