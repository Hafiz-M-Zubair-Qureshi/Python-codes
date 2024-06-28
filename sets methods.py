# add method (add an element)
# sets are mutable
# elements of sets are immmutale



# add method
collection=set()
collection.add(1)
collection.add(2.4)
collection.add(True)
collection.add("hello")
collection.add("world")
collection.add((1,2,3))

print(collection)





# remove method
collection=set()
collection.add(1)
collection.add(2.4)
collection.add(True)
collection.add("hello")
collection.add("world")
collection.remove(2.4)

print(collection)





# clear method
collection=set()
collection.add(1)
collection.add(2.4)
collection.add(True)
collection.add("hello")
collection.add("world")
collection.clear()

print(collection)





# pop method (remove random value)
collection={"hello","zubair","qureshi","world", "coding","python"}
print(collection.pop())



# union method (combines both set values and return new set value)
set1={1,2,3,4}
set2={3,4,5,6}

print(set1.union(set2))






# intersection method (combine common values of the set and return new set )
set1={1,2,3,4,5}
set2={3,4,5,6}

print(set1.intersection(set2))

