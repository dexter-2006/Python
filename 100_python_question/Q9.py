# 9. Write a program that take a user inputr of three angles and will find out whether it can form a
#  triangle or not.
x=float(input("angle 1 : "))
y=float(input("angle 2 : "))
z=float(input("angle 3 : "))

#if((x+y+z)<=180): # error must be equal to 180
if((x+y+z)==180):
    print("yes triangle is possible")
else:
    print("Not possible")