import random 

x = random.randrange(1,11)

for _ in range(3):
    guess = int(input("Guess the number between 1-10:"))
    if guess == x: 
        print("Correct!")
        break
    elif guess < x: 
        print("A little low")
    elif guess > x: 
        print("A little high")

print("The correct number was:", x)