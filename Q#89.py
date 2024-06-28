# By using list comprehension, please write a program to print the list
# after removing the value 24 in [12,24,35,24,88,120,155].




my_list=[12,24,35,88,120,155]             
after_comprehensiion_list=[num for num in my_list if num!=24]  # check condition by list comprehension
print(after_comprehensiion_list)               # print list after comprehension