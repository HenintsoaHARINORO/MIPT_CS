import turtle
import math
wn = turtle.Screen()
t = turtle.Turtle()
t.shape('turtle')
t.width(3)
t.color('red')
def sq(size):
    t.forward(size)
    t.left(90)

    t.forward(size)

    t.left(90)

    t.forward(size)
    t.left(90)
    t.forward(size)
def sqin(size):
    sq(size)
    t.left(90)
    t.penup()
    t.forward(size/2)
    t.left(45)
    t.pendown()
    sq(size*math.sqrt(2)/2)

sqin(100)


wn.exitonclick()