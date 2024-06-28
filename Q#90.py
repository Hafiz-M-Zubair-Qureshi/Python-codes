# With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list 
# whose elements are intersection of the above given lists.


def intersection(list1,list2):                  # define function
    list3=[num for num in list1 if num in list2]    # check the condition for intersection and store it in new list
    return list3                                     # return new list
list1=[1,3,6,78,35,55]
list2=[12,24,35,24,88,120,155]
print(intersection(list1,list2))                     # print same values of list1 and list2