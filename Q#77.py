# Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.




import random
my_even_numbers=[random.randrange(100,201,2) for i in range(5)]
print(my_even_numbers)