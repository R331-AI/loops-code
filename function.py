def raj(): # parameter
    print("this is a hello function")
raj()# basic code of function    

def sum(a,b): # parameter
    print(f"the sum of your number is {a+ b} ")
sum(12,23)
sum(44,55) # position argument

def raj(name,age): # parameter
    print(f"your name is {name } and your age is {age}")

raj(age = 20, name = "rajkumar")# this is a key word argument

def sum (a,b=33): # parameter
    print(f"the sum is {a+b}")
sum(12,2)    # this is difficult argument