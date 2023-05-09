import random 

x = random.randrange(1,1001)
attempts = 0

guess = int(input("Guess the number between 1-1000:"))
while(guess != x): 
    attempts += 1
    if guess < x: 
        print("Too low!")
    elif guess > x: 
        print("Too high!")
    guess = int(input("Guess the number between 1-1000:"))
print("The correct number was:", x)
print("It took you", attempts, "tires to get the number.")