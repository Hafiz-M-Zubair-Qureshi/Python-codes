# Please raise a RuntimeError exception.

# Hints:

# Use raise() to raise an exception.




def my_function():
    raise RuntimeError("this is a runtime error")  # here we use raise keyword. raise keyword is used to raise an exception or errors
try:
    my_function()
except RuntimeError:
    print("find an exception")





# Write a function to compute 5/0 and use try/except to catch the exceptions.


def divide_by_zero():
    try:
        result=5/0
    except ZeroDivisionError as e :
        print(f"caught an exception:{e}")
divide_by_zero()