# Please write assert statements to verify that every number in the list [2,4,6,8] is even.

# Hints:
# Use "assert expression" to make assertion.



my_list=[2,4,6,8]
for i in my_list:
    assert i%2==0, "{my_list} is not an even number"
print("All numbers are even")