#10. Write a program that will take user input of cost price and selling price and
#determines whether its a loss or a profit
x=int(input("cost price : "))
y=int(input("selling price : "))
if(x>y):
    print("loss")
else:
    print("profit")