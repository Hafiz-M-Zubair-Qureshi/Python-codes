# Write a program to generate and print another tuple whose values are even numbers in 
# the given tuple (1,2,3,4,5,6,7,8,9,10). 


my_tuple=(1,2,3,4,5,6,7,8,9,10)
even_number=tuple(x for x in my_tuple if x%2==0)
print(even_number)