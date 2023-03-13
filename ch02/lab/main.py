import random 
import turtle
import pygame 
import math

n = random.randrange(1,100)
x = random.randrange(1,100)
window = turtle.Screen()

cody = turtle.Turtle() 
brick = turtle.Turtle()
cody.shape("turtle")
brick.shape("turtle")
cody.color("blue")
brick.color("red")
cody.speed(1)
brick.speed(1)
cody.up()
brick.up()
cody.goto(-100,-20)
brick.goto(-100,20)
cody.down()
brick.down()
# race 1
cody.forward(n)
brick.forward(x)
cody.clear()
brick.clear()
cody.up()
brick.up()
cody.goto(-100,-20)
brick.goto(-100,20)
cody.down()
brick.down()

# race 2

for _ in range(10):
    go = random.randrange(1,11)
    cody.forward(go)
    yes = random.randrange(1,11)
    brick.forward(yes)

window.exitonclick()

## PART 2

pygame.init()
screen = pygame.display.set_mode()

num_sides = (3, 4, 6, 20, 100, 360)

for i in num_sides:
    points = []
    angle = 360/num_sides
    radians = math.radians(angle * i) 
    x = xpos + side_length * math.cos(radians)
    y = ypos + side_length * math.sin(radians)
    points.append((x,y)) 
    pygame.draw.poloygon(screen, "red", points)
    pygame.display.flip()
    pygame.time.wait(2000)



window.fill("blue")
pygame.display.flip()