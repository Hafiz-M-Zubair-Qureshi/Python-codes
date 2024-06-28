# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit 
# of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.






def find_even_digit_numbers(start,end):
    even_digit_numbers = []                # make empty array
    
    for i in range(1000, 3001):
       number_str = str(i)        # Convert the number to a string to check each digit
       if all(int(digit) % 2 == 0 for digit in number_str):       # check all digits is even or not
            even_digit_numbers.append(number_str)          # add elements in list after check the condition
    
    result = ",".join(even_digit_numbers)                  # convert to string
    return result

result = find_even_digit_numbers(1000, 3001)          # store values in result varibles in defined range
print(result)            # print the result varibles values

