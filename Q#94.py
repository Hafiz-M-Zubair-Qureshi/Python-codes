# Please write a program which accepts a string from console and print it in reverse order.



def reverse_string(my_string):
    reverse_string=my_string[::-1]
    print("Reversed string",reverse_string)

my_string=input("Enter your string:")
reverse_string(my_string)