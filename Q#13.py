# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3


string=input("Enter your sequence: ")             # input the sequence
Letter=0                           # initialize with 0
Digit=0                            # initialize with 0
for i in string:
    if (i.isalpha()):              #isalpha function check letter
        Letter+=1                  # increment letter
    elif i.isdigit():              # isdigit function check digit
        Digit+=1                   # increment digit
print(f"Letters is= {Letter}\nDigit is ={Digit}")  # here 'f' return the value of letter.and print the value of letter and digit

