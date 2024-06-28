# Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). 
# Then the function needs to print the last 5 elements in the list.


def my_list():
    list = [i*i for i in range(1,21)]
    new_list=list[15:]
    print(new_list)

my_list()