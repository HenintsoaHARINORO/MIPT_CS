# Вариант: 3
import turtle        # познакомили программу с библиотекой turtle
wn = turtle.Screen()
t = turtle.Turtle()
t.shape('turtle')
t.color('red','yellow')
t.begin_fill()

t.width(5)
t.left(36)
t.forward(200)

t.right(144)
t.forward(200)

t.right(144)
t.forward(200)

t.right(144)
t.forward(200)

t.right(144)
t.forward(200)


t.end_fill()
wn.exitonclick()