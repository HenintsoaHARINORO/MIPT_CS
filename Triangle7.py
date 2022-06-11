import turtle
wn = turtle.Screen()

def triangle():
    p0= t.pos()
    t.forward(100)
    p1=t.pos()
    t.goto(p0)

t = turtle.Turtle()

t.shape('turtle')
t.width(3)

wn.exitonclick()
