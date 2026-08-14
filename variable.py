# Note at the time of declaring variable in python we have assign value at the time
# declaration
# while in c/c++ we can declare after wards
#Python
# x wrong
# x=10 correct

# in c++
# int x; correct
# int x=10; both correct 

# in python we dont declare the data type of varibale like
# in c++ python interpertor automatically detects data type
# x = 10 integer data type

# but we can specifiy data type using
x=str(3) # string data type

y=int(3) # integer data type

z=float(3)# float data type

# to get the type of data we use 
# type()
print("data type of x = ",end="")
print(type(x))

print("data type of y = ",end="")
print(type(y))

print("data type of z = ",end="")
print(type(z))

# we can store string value in single '' as well as in double quote ""
b="nitin" # double quote
print(b)
c='nitin' # single quote
print(c)

# Variable rules declaration
# we can start we 
# letter alphabet and underscor
# a, b , _

# note we cannot start with number or digits
#1x wrong