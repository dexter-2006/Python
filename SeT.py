# list = [square bracket]
# tuple = (round bracket)
# set = {curly bracket} unordered

thisSet={"apple","banana","cheerry"}

# unordered 1) items in set do have defined order , the order in which we write is not the order we get
          # 2) items always store in different order , we never know
          # 3) we cannot refer element by index number
          # 4) set use hash table to store values that why order is not defined

# unchangeable 1) set items are unchangeable
             # 2) we cannot change the items after set has created
             # 3) but we can add and remove new items

# duplicates:- duplicates values are not allowed 
             # set cannot have two items with the same value
# TRUE and 1 are considered same value similar with FALSE and 0
h={"apple","bananan","apple","n","m"}
print(h) #in output the duplicate apple remove

# to add items in set we use
# add() method
set1={"a","b","nitin","aarav"}
set1.add("tarzan")
print(set1) # when you see the output you can order is not defined

set1.remove("b")
print(set1)

# to add two set
set2={"apple","banana","cherry","f","h"}
set3={"man","female","shatk","jungle"}
# now we want to add elements of set 3 in set 2
# we use update() method
set2.update(set3)
print(set2)

# we can add set with list,tuple.dictionaries

set44={"apple","mango","kiwi","jack","a"} # sets
tuple22=("a","l","aa","aaa","abaa") #tuple
set44.update(tuple22)#when you see the output also the order of element is random
print(set44)

# Remove set items 1) remove("string") give error if elements exist
                 # 2) pop(index) in set we cant have fixed index number for elements , so in set it remove random elements
                 # 3) discard()  does not give error if element not exist
area={"meter","inch","length","breadth","bigha","square"}
area.remove("inch")
print(area)
area.pop()
print(area)
area.pop()
print(area)

area.discard("length")

# to clear the set use .clear()
# to delete use del setname

# to join sets these methods are 1) union()
                               # 2) update()
                               # 3) intersection()
                               # 4) difference()
                               # 5) symmeteric difference()
# union() or |
st1={"a","b","c","d"}
st2=(1,2,3,4,33)
st3=st1.union(st2)
print(st3)

#st4=st1|st2
#print(st4)

# with union we can join set and tuple also

# update : update the set with items form other set
st1.update(st2)
print(st1)

# Intersection : it gives common elements / items present in two different sets
              # like intersection operation in maths
d1={"apple","jack","kite","yash","b"}
d2={"a","b","c","apple","love","sex"}
d3=d1.intersection(d2)
print(d3) # only apple and b will printed on command line

# intersectio_update() : it only keeps the duplicates but it will change the original set
d1.intersection_update(d2) # now d1 have only the elements which are in common
print(d1)
print(d2)

# Difference() : return elemets which are not present in first set
f1={"a","b","c","d","apple","bannana"}
f2={"b","c","oange","kite","tata","love"}
f3=f1.difference(f2)
print(f3)

# Difference_update() cahange the original set 
                   # remember the update always change the original keyword
# Symmetric_difference() it will give elements which are not present in both sets
g1={"a","b","apple","fuck"}
g2={"a","b","kuto","lito"}
g3=g1.symmetric_difference(g2)
print(g3)

# Symmetric_difference update change the original set

# Frozen set is immutable version of set where we cant add /remove elemets

x=frozenset({"apple","bananna"})
print(type(x)) #output frozen set

