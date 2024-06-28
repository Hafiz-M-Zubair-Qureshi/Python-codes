# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.



class demo():

    def _init_(self):
        self.string = ""

    def get_string(self):
        self.string = input("Enter the String: ")
    
    def print_string(self):
        my_string=self.string.upper()
        print(my_string)

def test_function():
    obj1 = demo()
    obj1.get_string()
    obj1.print_string()

test_function()