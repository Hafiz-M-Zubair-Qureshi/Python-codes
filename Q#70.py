# Please write a binary search function which searches an item in a sorted list. The function should return the
# index of element to be searched in the list.



def search(list,key,low,high):
    mid=(low+high)//2
    if list(mid)==key:
            return mid
    if list(mid) >key:
                search(list,key,low,mid-1)
    if list(mid) < key:
                search(list,key,mid+1,high)

list=[2,3,4,5,6,7,9876,234,765,123]
key=int(input("enter your number to search:"))
x=search(list,key,0,9)
if x==key:
    print("No found at index",x)