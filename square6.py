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


def sq2(size,n):
    p1 = t.pos()
    for i in range(n):
        sq(size,'green','red')
        sq(size, 'green', 'yellow')

    t.goto(p1)
    t.right(90)
    t.penup()
    t.forward(size)
    t.left(90)
    t.pendown()

##sq2(50,5)
def sq3(n,k):
    for i in range(k):
        sq2(50,n)

sq3(5,4)





wn.exitonclick()