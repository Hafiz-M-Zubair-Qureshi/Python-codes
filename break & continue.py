# ""break"" is used to "terminate the loop"
nums=(1,4,9,16,25,36,49,64,81,100)

x=49

i=0
while i<len(nums):
    if(nums[i]==x):
        print("Found at index",i)
        break
    else:
        print("Finding")
    i+=1
print("End of loop")




# continue ( terminates the current iteration and mov continuesously to the next iteration)
i=0
while i<=5:
    if(i==3):
        i+=1
        continue
    print(i)
    i+=1