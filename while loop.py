count=1
while count<=10:
    print("Zubair")
    count +=1
 


# print no from 1 to 100
i=1
while i<=100:
    print(i)
    i+=1
print("Loop ended")




# print no from 100 to 1
i=100
while i>=1:
    print(i)
    i-=1
print("Loop ended")




# multiplcation table of a number n
n=int(input("Enter your number: "))
i=1
while i<=10:
    print(n*i)
    i+=1
    


#  element of the following list using loop
nums=[1,4,9,16,25,36,49,64,81,100]
i=0
while i<len(nums):
    print(nums[i])
    i+=1




# search a number 'x' in tuple using loop (1,4 9,16,25,36,49,64,81,100)
nums=(1,4,9,16,25,36,49,64,81,100)

x=49

i=0
while i<len(nums):
    if(nums[i]==x):
        print("Found at index",i)
    else:
        print("Finding")
    i+=1

     