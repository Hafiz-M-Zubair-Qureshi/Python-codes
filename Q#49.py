# Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).


my_numbers=list(range(1,21))
square_number=list(map(lambda x:x**2,my_numbers))
print(square_number)