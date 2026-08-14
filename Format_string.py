# we cannot combine or add string and number directly

#age=36
#text="My name is John,I am"+age this will give error
#print(text)

# to add
 
# f"txt"{variable}"

age = 26
txt = f"the age of john is {age}"
#     f in first           {   }
print(txt)

# {} this curly braces is called placeholder
# in {} placeholder we can contain variables , operations,function,modifiers
name="harsh"
u= f"My name is {name}" # always remember to add f in first
print(u)

print(f"The sum of two number {3+4}")
