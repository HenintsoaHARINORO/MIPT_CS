import turtle
wn = turtle.Screen()

t = turtle.Turtle()

t.begin_fill()

t.color('blue','yellow')
t.width(5)
t.forward(75)

t.left(90)
t.color('violet','yellow')
t.forward(75)

t.left(90)
t.color('green','yellow')
t.forward(75)
t.left(90)
t.color('red', 'yellow')
t.forward(75)
t.left(90)
t.forward(75)
t.end_fill()

wn.exitonclick()
