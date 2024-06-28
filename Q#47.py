# Write a program which can map() and filter() to make a list whose elements are
# square of even number in [1,2,3,4,5,6,7,8,9,10].


my_list=[1,2,3,4,5,6,7,8,9,10]

even_numbers=filter(lambda x:x%2==0,my_list)    # using lamdha function to filter the list

square_even_numbers=map(lambda x:x**2,even_numbers)  # using lamdha function to map the filter values

result=list(square_even_numbers)     # store result in list
print(result)