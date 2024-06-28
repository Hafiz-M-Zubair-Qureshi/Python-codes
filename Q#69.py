# Please write a program which accepts basic mathematic expression from console and print the evaluation result.

# Example:
# If the following string is given as input to the program:
# 35+3
# Then, the output of the program should be:
# 38



mathematic_expression=input("enter your expression:")
try:
    my_result=eval(mathematic_expression)
    print(my_result)
except Exception as e:
    print(f"Error evaluating expression:{e}")



