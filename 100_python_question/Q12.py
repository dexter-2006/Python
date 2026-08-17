#12. Write a program to find the volume of the cylinder.
#Also find the cost when, when the cost of Ilitre milk is 40Rs.

x=int(input("Enter the radius: "))
y=int(input("Enter the height: "))
z=pow(x,2)
volume=(3.14*z)*y
print(f"volume:- {volume} meter cubic")

# 1 meter cubic = 1000l
# 1 liter = $40
# 1 liter = 1/1000 
cost= 1000*volume*40
print(f"cost of milk ${cost}")
