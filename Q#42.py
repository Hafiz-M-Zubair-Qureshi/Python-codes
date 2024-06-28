# With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line 
# and the last half values in one line.



tuple=(1,2,3,4,5,6,7,8,9,10)       # define tuple
tuple1=tuple[:5]                   # define first half of tuple by slicing
tuple2=tuple[5:]                   #  define second half of tuple by slicing
print(tuple1)
print(tuple2)