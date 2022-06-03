import turtle
wn = turtle.Screen()

t = turtle.Turtle()
t.shape('turtle')
t.width(3)

def sq():
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
def sq2():
    t.color('red')
    sq()
    t.right(90)
    t.penup()
    t.forward(50)
    t.right(90)
    t.right(45)
    t.pendown()
    t.color('blue')
    sq()
sq2()
wn.exitonclick()