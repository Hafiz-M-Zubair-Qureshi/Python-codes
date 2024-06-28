# Please write a program which accepts a string from console and print the characters that have even indexes.





def my_even_indexes(my_string):
    even_index_charactors=[my_string[i] for i in range(len(my_string))if i%2==0]
    print("Charactors of even index", ''.join(even_index_charactors))

my_string=input("Enter your string:")
my_even_indexes(my_string)