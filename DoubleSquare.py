import turtle
wn = turtle.Screen()

t = turtle.Turtle()

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

t.penup()
t.forward(50)
t.pendown()
t.begin_fill()

t.color('blue','violet')
t.width(5)
t.forward(75)

t.left(90)
t.color('blue','violet')
t.forward(75)

t.left(90)
t.color('blue','violet')
t.forward(75)
t.left(90)
t.color('blue','violet')
t.forward(75)
t.left(90)
t.end_fill()

wn.exitonclick()
