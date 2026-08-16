#sort is to sort elements in ascending order by default

thislist=["orange","apple","Zatana","lion","mango","Xmas"]
thislist.sort()
print(thislist)

# the capital letter have priority

num=[10,30,50]
num.sort()
print(num)

# to sort in descending order
# use reverse=True
print("to sort in descending order")
k=[10,90,100,101,103,104,103]
k.sort(reverse=True)
print(k)

#using function to sort
def myfunc(n):
    return abs(n-50)
thislist=[100,50,65,82,23]
thislist.sort(key=myfunc)
print(thislist)

#to print without capital letter protrity
thislist55=["Apple","manJo","gunja","Kalu"]
thislist55.sort(key=str.lower)
print(thislist55)

# Reverse()

# reverse() method is used to reverse the current sorthing order
# of the elements
listtits=["banana","ORANGE","Kiwi","Cherry","Mango"]
print(listtits) #this will print in correct order
listtits.reverse() #this will print in reverse order
print(listtits)

# Copy Lists
# we can copy list2=list1 to copy elements but changes in list1 will change the value 
# in list 2 also
# to solve this problem we use copy method()

cat=["apple","banana","cherry","daru"]
print(cat)
mycat=cat.copy()
print(mycat)

# to copy we can use list build in method list()

dog=["eat","sleep","rome","vito"]
mydog=list(dog)
print(mydog)
dog[1]=("harsh")
print(dog) # in this list 1 value changed
print(mydog) # but in this values are not changed

# we can use slice operator(:) also
money=["dollor","nepal","usa","jacl"]
mymoney=money[1:]
print(mymoney)

# Join Two lists

# Method 1= using + operator
list1=["a","b","c","d","e","f","g"]
list2=[1,2,3,"stringg"]
list3=list1+list2
print(list3)

# Method 2= by using append()
# it addd elemets one by one so we have to use loop

list3=["apkl","dmk","bjp","srm"]
list4=["chicken","eat","dinnert"]
#list5=list3.append(list4) # output none
#print(list5)

# we have to use for loop
for x in list4:
    list3.append(x) # append will add elements one by one
print(list3)

# Method 3= extend() 
# extend() adds all elements from another iterable (such as list tuple string)
# to the end of the current list
# extend() adds whole as single elements

list5=["piyus","ranjan","dsa","cn"]
list6=["jee","fate","gate","neet"]
list5.extend(list6)
print(list5)
