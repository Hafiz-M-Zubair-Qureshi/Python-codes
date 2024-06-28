# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world




n=str(input("Enter your sequence: "))
m=n.split(',')                        # convert the string to list
o=sorted(m)                           # sort in ascending order
a_sort=','.join(o)                    # convert to string
print(a_sort)
print(type(a_sort))
