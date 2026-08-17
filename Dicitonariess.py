# list=[square bracket] tuple=(round bracket) set={curly bracket}

# dictionaries store data in key value pairs

# ordered
# changeable : add() remove() change()
# Duplicates values are not allowed { same key value is not allowed}

thisdict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
print(thisdict)

# for lenght of dicitionaries
print(len(thisdict))

# To access dicitionary items

# Method 1: we can access by key name
x=thisdict["model"]
print(x)

# method 2 : .get("key name") using .get() function
y=thisdict.get("brand") # use curly bracket
print(y)

# Return list of keys () in dictionary
u={
    "name":"rajan",
    "age":25,
    "class":"10b",
    "height":"5foot",
    "address":"jharkhand"
}

# to get list of keys()
k=u.keys()
print(k)

# to get list of values use .values()
print(u.values())

# items() : return items in dicitionary as tuples
print("as tuples \n")
print(u.items())

# to check if key exists

student={
    "name":"orgy",
    "age":80,
    "number":"A+",
    "grade":90
}
if "name" in student:
    print("yes model is there")
else:
    print("no")

# to change dicitionary items

# Method 1: by using key name
student["name"]="jack"
print(student["name"])

# Method 2 : update()
student.update({"age":89})
print(student["age"])

# To add new elemets in dicitionary

kitchen={
    "home":"food",
    "door":"lock",
    "bathroom":"brush"
}

print(kitchen)

# method 1: use new key : value pair
kitchen["hall"]="tv"
print(kitchen)

# method 2: update() : change update/ exisiting key
                    # : add new key value pair
kitchen.update({"room":"bed"})
print(kitchen)

# removing items
# pop("key")

dict44={
    "brand":"Ford",
    "model":"Mustang",
    "year":2026,
    "spped":204
}

print(dict44)
dict44.pop("year")
print(dict44)

# popitem() : used to remove last inserted element
dict44.popitem()
print(dict44)

# del ["key"]
del dict44["model"]
print("dict")
print(dict44)

# del : delete the whole dicitionary

# clear() : empty the dicitionary 

# loop through dicitionary

girls={
    "name":"sony",
    "age":30,
    "class":12,
    "grade":"A+"
}

for x in girls:
    print(x) # only keys printed not values

# to print values one by one

for x in girls:
    print(girls[x]) # only values get printed

# to print only values use .values()
for x in girls.values():
    print(x)

# to return only key use .keys()
for c in girls.keys():
    print(c)

# to get both keys and values use items() method
print("to print key values\n")
for x,y in girls.items():
    print(x,y)

# copy dictionaries same 1) copy() method
#                        2) dict() function

# Nested Dictionaries

myfamily={
    "child1":{
        "name":"khushi",
        "year":2004
    },
    "child2":{
        "name":"yash",
        "age":90
    },
    "child3":{
        "name":"ishika",
        "year":2005
    }
}
print("myfamily here is the nested dicitionary\n")
print(myfamily)

print(myfamily["child2"]["age"])

# create three searate dicitionaries then create one dicitioary that will contain other
# 3 dicitionaries

son={
    "name":"alex",
    "age": 24
}
wife={
    "name":"gunja",
    "age": 45
}
grand={
    "name":"dada",
    "age":80
}
# here we combine all the dicitionary
family={
    "one":son,
    "t":wife,
    "k":grand
}
print(family)

