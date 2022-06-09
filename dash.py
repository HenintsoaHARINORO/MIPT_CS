import turtle
wn = turtle.Screen()
t = turtle.Turtle()
t.shape('turtle')
t.width(3)
t.color('red')
def dash(size):
    t.forward(size/2)
    t.penup()
    t.forward(size/2)
    t.pendown()
    t.forward(size/2)
def dtri(size):
    dash(size)
    t.left(120)
    dash(size)
    t.left(120)
    dash(size)

dtri(120)



wn.exitonclick()