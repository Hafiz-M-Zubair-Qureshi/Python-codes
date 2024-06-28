# keys method (return all outer keys not nested keys)
student={
    "name" : "Zubair",
    "subjects" : {
    "phy" : 65,
    "chem": 87,
    "math": 97,
    }
}
print(student.keys())
print(list(student.keys()))
print(len(list(student.keys())))



# value method ( return collection of all values)
student ={
    "name" : "Zubair",
    "sunjects" : {
        "phy" : "65",
        "chem" : "87",
        "math" : "97",
    }
}
print(student.values())
print(list(student.values()))



# item method(return all (key,values ) as tuples
student={
    "name" : "Zubair",
    "subjects" : {
    "phy" : 65,
    "chem": 87,
    "math": 97,
    }
}
print(student.items())
pairs=(list(student.items()))
print(pairs[0])
print(list(student.items()))




# get method (return the key accodring to value)
student={
    "name" : "Zubair",
    "subjects" : {
    "phy" : 65,
    "chem": 87,
    "math": 97,
    }
}
print(student["name"])
print(student.get("name"))
 
# print(student["name2"]) # error
print(student.get("name2")) # no error



# update method (insert the specified item to the dictionary)
student={
    "name" : "Zubair",
    "subjects" : {
    "phy" : 65,
    "chem": 87,
    "math": 97,
    }
}
student.update({"city" : "Multan"})
print(student)
