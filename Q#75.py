# Please write a program to output a random number, which is divisible by 5 and 7, between 0 and 10 inclusive 
# using random module and list comprehension.



import random
my_random_numbers=random.choice([i for i in range(0,11) if i%5==0 and i%7==0])
print(my_random_numbers)