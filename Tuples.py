# tuples=(curly bracket)
#the main difference is that it is immutable (we cant add,remove,change existing elemets)

# remembert tuple=(immutable

# all order thimngs are same as list so we are not discussing here

t=("apple","banana","liom","miot")
print(len(t)) #length of the tuple

# to create tuple with one item we have to coma(,) after the element
# without common ,
y=("apple")
print(type(y)) # output = string

y1=("apple",)
print(type(y1)) # output = tuple

# we cannot change the tuple values but if we want to change then follow
                                                                        # covert tuple to list
                                                                        # change 
                                                                        # covert list to tuple
x=("apple","banana","cherry")
# covert tuple to list
y=list(x) 
y[1]="KiWi"
#convert list to tuple
x=tuple(y)
print(x)

# To add elements into tuple 1) convert tuple into list
                           # 2) add elemets using list functiom
                           # 3) covert list into tuple
thistuple=("aPple","banana","cherry","orange")
y=list(thistuple) # convert tuple into list
y[1]="kashmir"
thistuple=tuple(y) # convert list into tuple
print(thistuple)

# we can add tuple to tuple if we want to add elemets to tuple
t4=("a","b","c","d","e","f","g")
t5=("last",)
t6=t4+t5
print(t6)

# to remove the elemenst from tuple we folloe 1) covert tuple into list
                                            # 2) remove /pop using list method
                                            # 3) change list to tuple
tuple1=("apple","banana","cherry","kite")
# tuple1.remove("kite") error
#covert tuple to list
list2=list(tuple1)
list2.remove("kite")
#covert list to tuple 
tuple1=tuple(list2)
print(tuple1)

# to del the tuple completely
ytuple=("a","b","1","3")
# ytuple.clear() error
print(ytuple)
del ytuple
#print(ytuple)

# Unpacking tuples/list
fruits=("apple","banana","cherry")
(a,b,c)=fruits # now a belongs to apple
               # b belongs to banana
               # c belongs to cherry
print(a)
print(b)
print(c)

# Asterisk *
# if no of variables assign for unpacking < is less than
# the items in tuple/list
# then we can use * to assign the remmaning value
fruit1=("apple","banana","watermelon","jack","jito","itio","lions")
(a,b,*c)=fruit1 # now a=apple b=banana c=watermelon,jack,jito etc the remaining will go into *
print(a)
print(b)
print(c)

# count() return no of items repeated
# syntax .count()
hash=("ku","tu","ku","tu")
print(hash.count("ku"))
