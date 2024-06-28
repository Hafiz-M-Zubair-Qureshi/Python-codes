# Define a class, which have a class parameter and have a same instance parameter.

class Car:
    
    parameter = "class value"

    def __init__(self,parameter):
        self.parameter = parameter
    
    def show(self):
        print(self.parameter)

obj = Car("instance_parameter")
obj.show()