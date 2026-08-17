#13. Write a program that will tell whether the given number is divisible by 3 & 6.
x=int(input("Enter num: "))
if(x%3==0 and x%6==0):
    print("Yes")
else:
    print("No")