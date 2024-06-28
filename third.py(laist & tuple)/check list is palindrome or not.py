list1=[1,2,3,2,3,1]

copy_list1=list1.copy()
copy_list1.reverse()

if(copy_list1==list1):
    print("Palindrome")
else:
    print("Not a palindrome")
