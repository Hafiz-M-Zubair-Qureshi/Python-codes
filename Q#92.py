# Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" 
# which can print "Male" for Male class and "Female" for Female class.



class Person:
    class Male:
        @staticmethod
        def Male():
            print("Male")
    class Female:
        @staticmethod
        def Female():
            print("Female")
obj=Person()
obj.Male().Male()
obj.Female().Female()