# in python string are stores as arrays

# we can access the string using index

name="HELLO"

print("The type of data type ",end="")
print(type(name))

print(name[0])

print(name[2])

for z in name:
    print(z)

# to print the length of string, list, tuple etc

# we use len()

print(len(name))

# to check the word or letter in sentence 
# we use in keyword

y= "H" in name
print(y)

text = "The independence day is on 15 august"

d= "day" in text
print(d)

if "independence" in text:
    print("yes")
else:
    print("no")

# slicing in string
# x[a:b] 
# not b is not included

print(name[0:3]) # 3 not included

print(text[2:8]) # 8 not included

# to start from 0 index use [:8]

# to end [2:]
print(name[0:])
print(text[:12])

# Negative slicing

print(name[-4:])

# modifing the string

# upper() for all upper case
# lower() to make all lower case
# strip() to remove white space

print(name.lower())
print(text.upper())

# to remove white space betweem sentences use strip

para = "The human mind has 80 bilion nurons"
print(para)
print(para.strip())

# to replace string we use keyword replace

c="mango"

print(c.replace("g","H")) # format replace("a","b")

# Sring concatenation : to add or concatenate we use + operator

print(name+c)

