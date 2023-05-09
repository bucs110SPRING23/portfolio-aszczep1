
x = int(input("Enter a number:"))
for i in range(x + 1):
   # if not i % 3 
    print("Number:", i)
    if i % 3 == 0 and i % 5 == 0: 
        print("fizzbuzz")
    elif i % 3 == 0: 
        print("fizz")
    elif i % 5 == 0: 
        print("buzz")