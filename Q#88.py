# By using list comprehension, please write a program to print the list after removing the 
# 0th,4th,5th numbers in [12,24,35,70,88,120,155].



my_list=[12,24,35,70,88,120,155]
comprehension_list=[my_list[i] for i in range(len(my_list)) if i not in (0,4,5)] # remove certain number by list comprehension
print(comprehension_list)