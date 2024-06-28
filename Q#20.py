# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a 
# given range 0 and n.


class number:                     # create class
    
    def generator(self,n):          # create generator function
        for i in range(n):
            if i%7 == 0:
                yield i
n=200
# n = int(input("Enter the range = "))
object1 = number()           # create object of class number
for i in object1.generator(n+1):
    print(i)