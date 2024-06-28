#Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then 
# check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma 
# separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010
# Notes: Assume the data is input by console.




bianry=input("enter a binary numbers of 4 digit with comma separated: ")
bianry_list=bianry.split(',')
for i in bianry_list:
    decimal_list=int(i,2)
    if(decimal_list%5==0):
        print(i,end="") 



# binary = input("Enter a sequence of comma separated 4 digit binary numbers: ")
# listOfBinary = binary.split(",")
# for i in listOfBinary:
#     binToDec = int(i,2)
#     if(binToDec%5 == 0):
#         print(i,end=" ")
