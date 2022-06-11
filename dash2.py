import turtle
wn = turtle.Screen()

def dash(col,n):
    for i in range(n):
        t.color(col)
        t.fd(50)
        t.penup()
        t.fd(25)
        t.pendown()

t = turtle.Turtle()

t.shape('turtle')
t.width(3)
dash('blue', 3)
dash('red', 2)
dash('green', 5)
wn.exitonclick()