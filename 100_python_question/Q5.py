#Write a program that will reverse a four digit number.Also it checks whether the reverse is true.
x=int(input("Enter four digit number:- "))
#z=x
org=x
t=0
a=1000
if(x>=1111 and x<=9999): # in this we can use len() also for shortcut
    i=1
    while i<=4:
        y=x%10
        print(f"y = {y}")
        z=int(x/10) #instead of converting int we can use // it return integer value
        x=z
        #print(z)
       #print(f"x = {x}")
        #a=1000
        t=t+(y*a)
        print(t)
        a=int(a/10) # //
        i+=1
else:
    print("error")
print(f"the reverse numb is {t}")

# we have to check also for plaindrome : means the number and its reverse are equal

if(t==org):
    print(f"yes plaindrome of {x} is {t} exist")
else:
    print("No plaindrome exist")

