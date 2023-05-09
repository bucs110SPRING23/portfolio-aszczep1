
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

# local variables get deleted outside of the function 
# functions must return a value like in math f(x) = y
# can only return one things 
def foo():
    x = 5
    return x
    # retun None: NoneType , what python returns if you don't retunr something in a function 

def bar(x = None): 
    if x is None: 
        x = 5 * 2


# nested functions execute from the inside out 

# case conventions 
# python uses: 
# def foo_bar():

# in a 10000 line program 
# name collisions 
# global variables never leave memory while the program is running 
