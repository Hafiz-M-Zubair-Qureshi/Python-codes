# Define a function that can accept two strings as input and print the string with maximum length in console.
# If two strings have the same length, then the function should print all strings line by line.



def maximum_length_string(string1,string2):
    if len(string1) > len(string2):
        print("First string is large:",string1)
    elif len(string2) > len(string1):
        print("Second string is large:",string2)
    else:
        print("First string is:",string1,"\nSecond string is :",string2)

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
maximum_length_string(string1,string2)