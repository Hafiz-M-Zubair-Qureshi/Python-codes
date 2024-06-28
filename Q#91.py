# With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all 
# duplicate values with original order reserved.



my_list=[12,24,35,24,88,120,155,88,120,155]           # create my list
new_set=set(my_list)                                  # convert it in set because remove all duplicate values
s=list(new_set)                                       # convert it in list
s.reverse()                                           # reverse the list
print(s)
