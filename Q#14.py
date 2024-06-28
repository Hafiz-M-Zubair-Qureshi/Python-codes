# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
#  UPPER CASE 1
# LOWER CASE 9





str="Helloworld"                  # store string
lower=0                           # in start lower variable=0
upper=0                            # in start upper variable=0
for i in str:
      if(i.islower()):           # islower() is built in funtion. this will check lower charactor
            lower+=1             # after check increment the lower charactor
      else:
            upper+=1             # after check condition increment the upper charactor
print("UPPER CASE:",upper)       # print the value of upper case
print("LOWER CASE:",lower)       # print the value of lower case