# Define a class named American and its subclass NewYorker.


class American:                      # create class
    class NewYorker:                 # create sub-class
        def __init__(self,city):
            self.city=city
            print(self.city)
obj=American()                    # create object
obj.NewYorker("city")

