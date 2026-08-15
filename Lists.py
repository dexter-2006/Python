# list [] mutable
# tuple() immutable
# set {}  mutable and undoreded because it uses heap memory
# dictionary {key:value} use key value pair

# thse are mainly four ways to store data

# list 
# used to store multiple items in a single variable
# ordered values are store in the order they are present
# changeable values can be changed
# allow duplicate values are allowed
# ordered
# changeable
# duplicate values

x=["banana","apple","orange"]
print(x)

# for length of the string use len()
print(len(x))

# in list we can store any data type
y=[1,2,3,4] #integer
t=[True,False,True] # bollean expresion

# we can store values of the multiple type also
u=["nitin",4,False,'A']
print(u)

print(type(u)) #by using type() function we can get the object like list,tuple etc

# List() Constructor
# Constructor is a function that creates object
thislist=list(("apple","banana","cherry"))
print(thislist)

# Access items

ff = ["hat","Gun","Bomb","jack"]
print(ff[0]) # remember always to use square bracket when using indexing
print(ff[2])

for x in ff:
    print(x)

# we can use range of index similar t slicing
print(ff[0:2])

# to check id the item or element exist in list or not use 
# in keyword
if "hat" in ff:
    print("yes")


# we can change the item
oo = ["dog","cat","kite","cow"]
# to change the kite to frog 
oo[2]="frog"
for x in oo:
    print(x)

# we can change range of item also by using method of slicing

ii = ["a","b","c","d","e","f","g","h","i","j","k","l"]
for x in ii:
    print(x)
# to change the value from index 1 to index 5
ii[4:6]=["mango","watermelon"]
for x in ii:
    print(x)

# to insert the value at specific index or position use
# use insert() keyword to insert new item without replacing the exisiting item
# syntax .insert(2,"spacex")
#.            (position," ")

ii.insert(2,"spaceX")
for x in ii:
    print(x)

# append() to add elements items list tuple sets etc at the end 
# just use .appen("")

uu=["apple","Banana","cherry"]
uu.append("khushi") #this will add the end

for x in uu:
    print(x)

# we can also add tupel
ws=("tanya","insha","gautam")
uu.append(ws) # if we use append to add list but try to use extend()
for x in uu:
    print(x)

# to add another list to current list we use
# extend() keyword

yt=["man","dog","cat"]
op=["cricket","chutiya","bbci"]
yt.extend(op)
for x in yt:
    print(x)

# we can add list and tuple

w1=["a","f","teeth"]
w2=(1,2,3,4,5) # tuple
w1.extend(w2)
for x in w1:
    print(x)

# append() to add specific element at last
# extend() to add list/tuple at last

# .remove() to remove specific item/elememt from the list

l2=["apple","banana","yash","orange"]
l2.remove("yash")
for x in l2:
    print(x)
print("\n\n")
print("pop")
# .pop(n) to remove element/item from specific index
# just mentioned the index number
l3=[1,2,3,4,5,6,7]
l3.pop(1) #at index 1 the elemet will removed

for x in l3:
    print(x)
# note: if we want to remove last element just use .pop()
#.                                                 no speici the index number
l2.pop() # last element directly removed
l3.pop()

for x in l2:
    print(x)
for x in l3:
    print(x)
 # the difference betweem .remove() and .pop()
 # is that both used to remove element but .remove() used to remove string directly
 # pop() is used to remove element directly by using index

 # remove("string")
 # pop(index)

# del keyword 
# to delete element
# to delete list completely
print("del keyword")
y1=["apple","banana","cherry","orange"]
del y1[1]
#del y1["apple"] del keyword also index based deletion
for x in y1:
    print(x)

# to delete the list completly
del y1
# print(y1) this will delete the list completely

# clear() used to clear the elements from the list
print("clear()")
t1=["apple","bag","kota","lion"]
t1.clear() # this will not delete the list completely but clear the elemets present in it
print(t1)

print("Loop through Index number")

i0=["harsh","lion","kito","tomato"]
for i in range(len(i0)):
    print(i0[i])

# while loop i=0 declare it we dont have inbuild in
#            len() used to determine the length of the list
print("While loop in python")
y9=["apple","orange","iota"]
i=0
while i < len(y9):
    print(y9[i])
    i=i+1
print("Loop usign Comprehension")
# Loop using comprehesion
fuck=["sunny","burj","lana"]
[print(x) for x in fuck]


