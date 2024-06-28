# By using list comprehension, please write a program to print the list after removing the  
# 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].



my_list=[12,24,35,70,88,120,155]
comprehension_list=[my_list[i] for i in range(len(my_list)) if i not in (0,2,4,6)]
print(comprehension_list)