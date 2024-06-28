# Please write a program to output a random even number between 0 and 10 
# inclusive using random module and list comprehension.



import random
my_even_numbers=random.choice([i for i in range(0,11,2)])  # here random.choice is used the functionality of 
                # random.choice is that its selected the element in the list which are even number in defined range
print(my_even_numbers)




