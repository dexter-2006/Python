# if we want to change the value of 
# global variable then we have to use global keyword

x=10 # global varibale

def change():
    global x # it is used to change the value of global varibale value
    x=20
    print(x)

change()