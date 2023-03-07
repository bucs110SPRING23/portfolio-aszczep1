
# vending machines 
# black boxing 
# functions are always called in a global scope 
#print("Welcome to the vending machine")
#code = input("Please enter a code")
#money = input("give me money:")

# a function should never be responsible for input 

def find_max(): 
    print("please enter 3 numbers")
    a = int(input(": "))
    b = int(input(": "))
    c = int(input(": "))

    max = a 
    if b > max: 
        max = b
    if c > max: 
        max = c

    print(max)

find_max()

# collisons 
# two variables of the same name 
# can't have variables of the same name in the same name 

