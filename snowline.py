import turtle
wn = turtle.Screen()
t = turtle.Turtle()
t.shape('turtle')
t.width(3)
t.color('blue')
def snowline(x):
    t.forward(2 * x)
    t.left(45)
    t.forward(x)
    t.backward(x)
    t.right(45)
    t.forward(x)
    t.backward(x)
    t.right(45)
    t.forward(x)

snowline(100)


wn.exitonclick()