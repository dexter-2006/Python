# input() takes as string 
# if we want integer value then we have to convert in into int

print("Enter name:- ")
x=input()
print(x)

# or we can take using input as argumnet

name=input("there we have argument to print:- ")
print(name)

# to take integer value
age=int(input("enter your age babay:- "))
print(age)

price=float(input("enter in gram in decimal"))
print(price)

# to take multiple values at the same line 
# then we have to map() and split()
# a,b=map(int,input().split())
# print(f"a is :- {a}")
# print(f"b is :- {b}")

# input inside loop
n=int(input())
for i in range(n):
    x=int(input())
    print(x)