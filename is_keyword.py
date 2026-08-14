# identity operator
#in identity operator there are two things

# first one is 
# == this checks if the values are equal of not ex 5==5 
# is operator checks if both variable points to the same object in the memory

# x is y return true if both belongs to same object

x = 5
y = 5

print(x is y) # this will return true because for small integer value python
              # does not create two differt object
              # we can see this by using id() its gives unique identification number
              # for object 
print(id(x))
print(id(y))

g=["apple","banana"]
h=["apple","banana"]

print(g is h) # this will return false beacuse python creates two different
              # two different objects 
              # we can see by id() function
print(g==h)   # this will return true because equal to operator compares the values
print(id(g))
print(id(h))

# now == equal to operator
print(x==y)
print(g==h)

z=y
print(x is z) # now this will return true because now they are pointing to same object

# is not keyword return true if both varaible does not point to same object
print(g is not h)

# in (x in y) keyword return true if sequence with specified value is present in the sequence
# not in( x not in y) return true if sequence of character or string does not present in the sequence
