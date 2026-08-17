# Q7) Write a program that will tell whether the given year is a leap year or not.

# the year is divisible by 400, it is a leap year. 
# Otherwise, if the year is divisible by 100, it is not a leap year. 
# Otherwise, if the year is divisible by 4, it is a leap year. 
# Otherwise, it is not a leap year.
x=int(input("Enter year: "))
if(x%400):
    print("Leap year")
elif(x%100):
    print("Not leap year")
elif(x%4):
    print("Leap year")
else:
    print("Not leap year")