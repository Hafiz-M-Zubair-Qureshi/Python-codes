# Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].



my_list=[1,2,3,4,5,6,7,8,9,10]
def even_number(n):
    return n%2==0

my_even_numbers=filter(even_number,my_list)
print(list(my_even_numbers))