# Define a function which can generate and print a list where the values are square of numbers
# between 1 and 20 (both included).


def my_list():
    list = [i*i for i in range(1,21)]
    print(list)

my_list()