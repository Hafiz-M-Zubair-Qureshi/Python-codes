# Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.



import random
my_list=[random.randint(100,200) for i in range(5)]
print(my_list)