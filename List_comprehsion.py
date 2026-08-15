# LIST COMPREHSION
# means to create new list based on the values present in the exisiting list

# based on list of fruits if we want to create list with only fruits with letter a

# we can do by two method 1) using for
                        # 2) list comprehsion

# METHOD 1: for loop
fruits=["apple","banana","cherry","kiwi","mango","papaya"]
newlist=[] # this is list because we have used square bracket

for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)

# METHOD 2: comprehension
# newlist=[expression for item in iterable if condition==true]
print("comrehension Method")
fruits1=["apple","banana","cherry","kiwi","mango"]
newList1=[x for x in fruits1 if "a" in x]
#I confuse in syntax
print(newList1)

# if we want to add elements in the new list from exisiting list directly

title=["siggh","yash","kapoor","toto"]

titlenew=[x for x in title]
print(titlenew)


# range method to use with comprehesion

print("Range method to use with comprehesion")
group=[x for x in range(10)]
print(group)

group1=[x for x in range(100) if x%2]

# syntax just add condition at the last
print(group1)

# to change the expression

#print("to change the expression")
ran=["fruits","apple","banna","lotus"]
newran=[x.upper() for x in fruits]
print(newran)

print("to return orange in place of banana")
tit=["apple","banana","cherry","orange","guava"]
titnew=[x if x!="banana" else "orange" for x in fruits]
print(titnew)

# bro I am not understanding the syntax
