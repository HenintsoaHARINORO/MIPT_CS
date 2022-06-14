import turtle
import math
wn = turtle.Screen()
t = turtle.Turtle()
t.shape('turtle')
t.width(3)

def sq(size,col,col3):
    t.begin_fill()
    t.color(col, col3)
    for i in range(4):
        t.forward(size)
        t.left(90)
    t.penup()
    t.forward(size)
    t.pendown()

    t.end_fill()

def sq1(size):
    for i in range(5):
        sq(size, 'green', 'yellow')
        sq(size, 'green', 'red')
def sq3(size):
    for i in range(5):
        sq(size, 'green', 'red')
        sq(size, 'green', 'yellow')

def sq4():
    p1 = t.pos()
    for i in range(1):
        sq3(50)
        t.goto(p1)
        t.right(90)
        t.penup()
        t.forward(50)
        t.left(90)
        t.pendown()
        p2= t.pos()
        sq1(50)
        t.goto(p2)
        t.right(90)
        t.penup()
        t.forward(50)
        t.left(90)
        t.pendown()
def sq5(n):
    for i in range(n):
        sq4()
sq5(4)






wn.exitonclick()