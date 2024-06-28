list=[1,2,3]
for el in list:
    print(el)




#  element of the following list using loop
nums=[1,4,9,16,25,36,49,64,81,100]
for el in nums:
    print(el)




# search a number 'x' in tuple using loop (1,4 9,16,25,36,49,64,81,100)
nums=(1,4,9,16,25,36,49,64,81,100,49)
x=49

i=0
for el in nums:
    if(el==x): 
        print("number found at index",i)
    i+=1
