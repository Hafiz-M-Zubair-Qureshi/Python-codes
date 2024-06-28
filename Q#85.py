# By using list comprehension, please write a program to print the list after removing delete numbers which are
#  divisible by 5 and 7 in [12,24,35,70,88,120,155].



my_list=[12,24,35,70,88,120,155]
After_compehension_list=[num 
                        for num in my_list if not(num%5==0 and num%7==0)]
print(After_compehension_list)