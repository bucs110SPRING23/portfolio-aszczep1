import turtle

pen = turtle.Turtle()
pen2 = turtle.Turtle()
pen.color("orange")
pen2.color("purple")
pen.shape("turtle")
pen2.shape("turtle")
pen.speed(1)
pen2.speed(0)

window = turtle.Screen()

pen.forward(100)



#interface: what can I tell it to do, abstract away the details
#state 

#always must be the last turtle command
window.exitonclick()