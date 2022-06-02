import turtle
wn = turtle.Screen()

t = turtle.Turtle()


t.color('violet', 'green')


t.begin_fill()

t.width(5)
t.left(45)
t.forward(100)
t.right(45)
t.forward(100)
t.left(-135)
t.forward(100)
t.left(-45)
t.forward(100)

t.end_fill()

wn.exitonclick()
