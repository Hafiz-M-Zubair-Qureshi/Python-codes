# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT



# str=input("Enter the string: ")
# str1=str.upper()
# print(str1)
# print(type(str1))


def capitalize_lines():
    lines = []              # Read input lines
    print("Enter your string :")
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    
    capitalized_lines = [line.upper() for line in lines]     # Capitalize each line
    
    for line in capitalized_lines:
        print(line)        # Print the capitalized lines

capitalize_lines()





