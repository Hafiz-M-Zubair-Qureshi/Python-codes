# key of dictionary is always string but we can also use integer, floating, tuple but we can't use list.   we can also make null,empty dict.
info= {
    "name": "Zubair",
    "age" : 21,
    "subjects" : ["python", "C", "Java"],
    "cgpa" : 3.50,
    "topics" : ("dict" ,"set"),
    "is_adult" : True,
}

info["name"] = "Qureshi" 
info["surname"] = "Bhai"
print(info)
print(info["name"])
print(info["age"])
print(info["subjects"])
print(info["cgpa"])
print(info["topics"])
print(info["is_adult"])
print(info["surname"])