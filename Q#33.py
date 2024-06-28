# Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and 
# the values are square of keys.



def keys_square():              # define function
    dict = {}                    # define dictionary
    for i in range(1,4):         # loop in specific range
        dict[i] = i**2           # square the values
    print(dict)
keys_square()                    # call function