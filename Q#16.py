# Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
# Suppose the following input is supplied to the program:
# 1,2,3,4,5,6,7,8,9
# Then, the output should be:
# 1,9,25,49,81


n=input("Enter the sequence of comma separated numbers:")
converted_list=[int(x)                               # convert string into integers list
                for x in n.split(",")
]
square_odds_no=[x**2                          # use comprehension list for the square of all odd numbers
                for x in converted_list
                if(x%2!=0)]
print(square_odds_no)