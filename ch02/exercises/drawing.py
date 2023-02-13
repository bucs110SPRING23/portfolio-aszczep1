import turtle
sides = input("Number of sides:")
sides = int(sides)

length = int(input("Enter length of sides:"))

rob = turtle.Turtle()
window = turtle.Screen()
rob.shape("turtle")
rob.color("blue")

for s in range(sides): 
    rob.forward(length)
    rob.right(360/sides)

window.exitonclick()