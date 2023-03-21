import turtle
import random 

def star(pos): 
    '''
    Draws star shapes
    args: pos:(tuple) coodinates for the star)
    '''
    star = turtle.Turtle()
    star.up()
    star.goto(pos)
    star.down()
    star.ht()
    star.color("yellow")
    sides = 5
    star.begin_fill()
    for s in range(sides): 
        star.left(108)
        star.forward(5)
        star.right(36)
        star.forward(5)
    star.end_fill()   


def star_place(amt_stars = 2, wn = None):
     '''
     Creates the coordinates for the stars at random. 
     args: amt_stars:(int) coordinates in dict, wn:(turtle_Screen)
     returns: a dictionary of random x:y coodinates to turtle window
     '''
     wn.setworldcoordinates(0,0,300, 300)
     star_pos = {}
     for i in range(amt_stars):
        x_cor = random.randint(20, 250)
        y_cor = random.randint(20, 250)
        pos = (x_cor, y_cor)
        star_pos[x_cor] = y_cor
     return star_pos
       
         
def circles(x, y, radius): 
    '''
    Draws cirles using turtle(). 
    args: x:(int) x coordinate, y:(int) y coordinate, radius:(int) length of the circle
    return: NULL
    '''
    moon = turtle.Turtle()
    moon.ht()
    moon.up()
    moon.goto(x, y)
    moon.down()
    moon.color("yellow")
    moon.begin_fill()
    moon.circle(radius)
    moon.end_fill()


def main(): 
    wn = turtle.Screen()
    wn.bgcolor("black")
    star_pos = star_place(5, wn)
    for k, v in star_pos.items():
        pos = (k, v)
        star(pos)
    circles(260, 240, 40)
    star_pos = star_place(12, wn)
    for k, v in star_pos.items():
        radius = 2 
        circles(k, v, radius)
    wn.exitonclick()

main()