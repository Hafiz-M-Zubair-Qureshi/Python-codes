# Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).



my_numbers=list(range(1,21))

even_numbers=list(filter(lambda x:x%2==0,my_numbers))

print(even_numbers)