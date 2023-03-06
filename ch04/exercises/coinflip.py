import turtle 
import random


joe = turtle.Turtle()
window = turtle.Screen()
joe.shape("turtle")
joe.color("blue")
screen_size = window.screensize()
print(screen_size)
is_in_screen = True

while is_in_screen:
    side = random.randrange(0,2)
    if side: 
        joe.left(90)
    elif side:
        joe.right(90)
    joe.forward(50)
    
    joeX = joe.xcor()
    joeY = joe.ycor()

    x_range = window.window_width() / 2
    y_range = window.window_height() / 2

    if abs(joeX) > x_range or abs(joeY) > y_range: 
        is_in_screen = False 

window.exitonclick()
