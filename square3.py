import turtle
import math
wn = turtle.Screen()
t = turtle.Turtle()
t.shape('turtle')
t.width(3)

def sq(size,col):
    t.color(col)
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size)
def sqin(size,col1,col2):
    sq(size,col1)
    t.left(90)
    t.penup()
    t.forward(size/2)
    t.left(45)
    t.pendown()
    sq(size*math.sqrt(2)/2, col2)

sqin(100,'blue', 'black')


wn.exitonclick()