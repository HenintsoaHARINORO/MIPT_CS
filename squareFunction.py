import turtle
wn = turtle.Screen()

t = turtle.Turtle()

def square():
    t.begin_fill()

    t.color('red','yellow')
    t.width(5)
    t.forward(75)
    t.left(90)
    t.color('red','yellow')
    t.forward(75)
    t.left(90)
    t.color('red','yellow')
    t.forward(75)
    t.left(90)
    t.color('red', 'yellow')
    t.forward(75)
    t.left(90)
    t.forward(75)
    t.end_fill()

square()
t.backward(75)
t.left(45)
square()
t.backward(75)
t.left(45)
square()

wn.exitonclick()
