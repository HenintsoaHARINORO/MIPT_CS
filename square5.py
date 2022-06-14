import turtle
import math
wn = turtle.Screen()
t = turtle.Turtle()
t.shape('turtle')
t.width(3)

def sq(size,col,col3):
    t.begin_fill()

    t.color(col, col3)
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.end_fill()
def sqin(size,col1,col2,col3,col4):
    sq(size,col1,col3)
    t.left(90)
    t.penup()
    t.forward(size/2)
    t.left(45)
    t.pendown()
    sq(size*math.sqrt(2)/2,col2,col4)
    t.backward(size*math.sqrt(2)/4)
    t.left(45)

def sqn1(size,n):
    for i in range(n):
        sqin((size/(math.pow(2,i))),'blue', 'red','green','yellow')
sqn1(400,5)





wn.exitonclick()