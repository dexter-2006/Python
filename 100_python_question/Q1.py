#1. User will input (3ages).Find the oldest one 
x=int(input("Enter age of one:= "))
y=int(input("Enter age of two:= "))
z=int(input("Enter age of three:= "))

if(x>y and x>z):
    print(" x is oldest")
elif(y>x and y>z):
    print("y is oldest")
elif(z>x and z>y):
    print("z is oldest")
else:
    print("error")