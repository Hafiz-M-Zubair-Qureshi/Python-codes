# recursive function
# print 5 to 1 by recursion function
def show(n):
    if(n==0):  # base case means where the condition stops
        return
    print(n)
    show(n-1)

show(5)    



# find factorial through recursive function
def fact(n):
    if (n==1 or n==0):
        return 1
    return fact(n-1) * n
print(fact(5)) 




# recursive funtion to calculate the sum of first n natural number
def calc_sum(n):
    if(n==0):
        return 0
    return calc_sum(n-1) +n
print(calc_sum(6))



# recursive function to print all element in a list ( use list & index as parameters)
def print_list(list,index=0):
    if(index==len(list)):
        return 
    print(list[index])
    print_list(list,index+1)
fruits=["mange","banana","apple","litchi"]
print_list(fruits)