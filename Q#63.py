# Write a program to compute:
# f(n)=f(n-1)+100 when n>0
# and f(0)=1
# with a given n input by console (n>0).

# Example:
# If the following n is given as input to the program:
# 5
# Then, the output of the program should be:
# 501
# In case of input data being supplied to the question, it should be assumed to be a console input.




def f(n):
    if n == 0:
        return 1
    else:
        return f(n-1) + 100

n = int(input("Enter the number = "))
my_result = f(n)
print(my_result)